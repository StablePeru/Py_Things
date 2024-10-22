# Word Searcher Application

A simple, user-friendly word searcher built using PyQt5 and Python. This application allows users to search for specific words or phrases across multiple file formats (TXT, DOCX, PDF) within a selected folder. It also provides options to view, open, and export the search results.

## Features

- **Search Across Multiple Formats**: Search for words or phrases in `.txt`, `.docx`, and `.pdf` files.
- **Folder Selection**: Easily select the folder in which to search for your desired word or phrase.
- **Progress Bar**: Track the progress of the search process in real-time.
- **Results Display**: View the search results in a list, including the file name, line number, and the content where the word was found.
- **Open Files**: Open the files containing the search result with a single click.
- **Export Results**: Export search results to a CSV or text file for future reference.

## Technologies Used

- **Python**: Core programming language used for this application.
- **PyQt5**: GUI toolkit used to create the application's user interface.
- **PyMuPDF (fitz)**: Library used to extract text from PDF files.
- **python-docx**: Library used to read `.docx` files.
- **CSV**: Built-in Python module used to export search results.

## Installation

### 1. Clone the Repository

Clone the repository:

```sh
git clone https://github.com/StablePeru/Py_Things/tree/main/WordSearcher.git
```

Change directory to the project folder:

```sh
cd WordSearcher
```

### 2. Create a Virtual Environment (Optional but Recommended)

Create a virtual environment:

```sh
python -m venv venv
```

**Activate the Virtual Environment**:

On Linux/macOS:
```sh
source venv/bin/activate
```

On Windows:
```sh
venv\Scripts\activate
```

### 3. Install Dependencies

Install the required dependencies:

```sh
pip install -r requirements.txt
```

### 4. Run the Application

Run the application:

```sh
python word_searcher.py
```

## Usage

- **Select a Folder**: Click on "Select Folder" to choose the directory in which to search.
- **Enter the Word or Phrase**: Type the word or phrase you want to search for in the provided text input box.
- **Start the Search**: Click "Search" to begin the search process. The progress bar will update as the search progresses.
- **View Results**: The results will be displayed in a list with the file name, line number, and the content snippet.
- **Open a File**: Click on any result to open the corresponding file using the default application.
- **Export Results**: Click "Export Results" to save the search results to a CSV or text file.

## Requirements

- Python 3.6+
- PyQt5
- PyMuPDF
- python-docx

You can install the required packages using the following command:

```sh
pip install PyQt5 PyMuPDF python-docx
```

## Contributing

Contributions are welcome! If you have any improvements or suggestions, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- **StablePeru** - [GitHub Profile](https://github.com/StablePeru)

Feel free to reach out with any questions or suggestions regarding this project!

