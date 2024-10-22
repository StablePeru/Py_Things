import os
import re
import sys
import fitz  # PyMuPDF
import docx
import threading
import time
import csv
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QFileDialog, QMessageBox, QProgressBar

class WordSearcher(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set up the user interface
        self.setWindowTitle('Word Searcher in Files')
        self.setGeometry(100, 100, 800, 600)

        # Main layout
        layout = QtWidgets.QVBoxLayout()

        # Button to select folder
        self.btn_select_folder = QtWidgets.QPushButton('Select Folder')
        self.btn_select_folder.clicked.connect(self.select_folder)
        layout.addWidget(self.btn_select_folder)

        # Text input to enter the word to search
        self.input_word = QtWidgets.QLineEdit(self)
        self.input_word.setPlaceholderText('Enter the word or phrase to search...')
        layout.addWidget(self.input_word)

        # Button to start the search
        self.btn_search = QtWidgets.QPushButton('Search')
        self.btn_search.clicked.connect(self.start_search)
        layout.addWidget(self.btn_search)

        # Progress bar
        self.progress_bar = QProgressBar(self)
        self.progress_bar.setValue(0)
        layout.addWidget(self.progress_bar)

        # List to display the results
        self.results_list = QtWidgets.QListWidget()
        self.results_list.itemClicked.connect(self.open_file)
        layout.addWidget(self.results_list)

        # Button to export results
        self.btn_export = QtWidgets.QPushButton('Export Results')
        self.btn_export.clicked.connect(self.export_results)
        layout.addWidget(self.btn_export)

        # Set the layout
        self.setLayout(layout)

    def select_folder(self):
        # Open a dialog to select a folder
        folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        if folder:
            self.folder = folder

    def start_search(self):
        # Clear previous results
        self.results_list.clear()

        # Get the word to search
        word = self.input_word.text()
        if not word:
            QMessageBox.warning(self, 'Warning', 'Please enter a word or phrase to search.')
            return

        # Perform the search in a separate thread
        if hasattr(self, 'folder'):
            self.progress_bar.setValue(0)
            self.results = []
            self.thread = threading.Thread(target=self.search_word, args=(self.folder, word))
            self.thread_finished = False
            self.thread.start()
            self.monitor_timer = QtCore.QTimer()
            self.monitor_timer.timeout.connect(self.monitor_search)
            self.monitor_timer.start(100)
        else:
            QMessageBox.warning(self, 'Warning', 'Please select a folder first.')

    def monitor_search(self):
        # Monitor the search thread and update the progress bar
        if not self.thread.is_alive():
            self.monitor_timer.stop()
            self.progress_bar.setValue(100)
            for result in self.results:
                item = QtWidgets.QListWidgetItem(f"{result['file']} (Line {result['line']}): {result['content']}")
                item.setData(1, result)  # Store the result information
                self.results_list.addItem(item)
        else:
            self.progress_bar.setValue(min(self.progress_bar.value() + 5, 100))

    def search_word(self, folder, word):
        # Compile the regular expression for the word to search
        pattern = re.compile(word, re.IGNORECASE)

        # Walk through all files in the selected folder
        for root, _, files in os.walk(folder):
            for file in files:
                file_path = os.path.join(root, file)
                if file.endswith('.txt'):
                    self.results.extend(self.search_in_txt(file_path, pattern))
                elif file.endswith('.docx'):
                    self.results.extend(self.search_in_docx(file_path, pattern))
                elif file.endswith('.pdf'):
                    self.results.extend(self.search_in_pdf(file_path, pattern))

    def search_in_txt(self, file_path, pattern):
        # Search for the word in a .txt file
        results = []
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
            for line_number, line in enumerate(lines, start=1):
                if pattern.search(line):
                    results.append({'file': file_path, 'line': line_number, 'content': line.strip()})
        return results

    def search_in_docx(self, file_path, pattern):
        # Search for the word in a .docx file
        results = []
        doc = docx.Document(file_path)
        for line_number, paragraph in enumerate(doc.paragraphs, start=1):
            if pattern.search(paragraph.text):
                results.append({'file': file_path, 'line': line_number, 'content': paragraph.text.strip()})
        return results

    def search_in_pdf(self, file_path, pattern):
        # Search for the word in a .pdf file
        results = []
        with fitz.open(file_path) as pdf:
            for page_number, page in enumerate(pdf, start=1):
                text = page.get_text()
                for line_number, line in enumerate(text.split('\n'), start=1):
                    if pattern.search(line):
                        results.append({'file': f"{file_path} (Page {page_number})", 'line': line_number, 'content': line.strip()})
        return results

    def open_file(self, item):
        # Open the selected file with the default application
        result = item.data(1)
        file_path = result['file'].split(' (Page ')[0]  # Get the path without page details
        if os.path.exists(file_path):
            try:
                os.startfile(file_path)
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'Could not open the file: {str(e)}')
        else:
            QMessageBox.warning(self, 'Error', 'The file is not available.')

    def export_results(self):
        # Export the search results to a CSV or text file
        if not self.results:
            QMessageBox.information(self, 'Information', 'No results to export.')
            return

        file_path, _ = QFileDialog.getSaveFileName(self, 'Save Results', '', 'CSV Files (*.csv);;Text Files (*.txt)')
        if file_path:
            with open(file_path, 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(['File', 'Line', 'Content'])
                for result in self.results:
                    writer.writerow([result['file'], result['line'], result['content']])
            QMessageBox.information(self, 'Information', 'Results exported successfully.')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    searcher = WordSearcher()
    searcher.show()
    sys.exit(app.exec_())
