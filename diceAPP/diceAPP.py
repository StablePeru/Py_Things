import random
import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from datetime import datetime

# Function to simulate rolling a die
def roll_dice():
    return random.randint(1, 6)

# Function to animate the die roll before displaying the final result
def animate_dice(label, log_widget):
    animations = [
        "⚀", "⚁", "⚂", "⚃", "⚄", "⚅"
    ]
    # Show random die faces for a short period to create an animation effect
    for _ in range(10):
        label.setText(random.choice(animations))
        QtWidgets.QApplication.processEvents()
        QtCore.QThread.msleep(100)
    # Get the final roll result and display it
    result = roll_dice()
    display_dice(label, result)
    log_result(log_widget, result)

# Function to display the final die face based on the result
def display_dice(label, result):
    dice_faces = {
        1: "⚀",
        2: "⚁",
        3: "⚂",
        4: "⚃",
        5: "⚄",
        6: "⚅"
    }
    label.setText(dice_faces[result])

# Function to log the result of the die roll with a timestamp
def log_result(log_widget, result):
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_widget.append(f"{current_time} - Result: {result}")

# Function to handle the roll button click event
def roll():
    animate_dice(result_label, log_text)

# Function to handle the exit button click event
def close_app():
    app.quit()

# Create the application and main window
app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Dice Simulator")
window.setGeometry(100, 100, 400, 500)

# Set up the layout
layout = QtWidgets.QVBoxLayout()

# Welcome label
welcome_label = QtWidgets.QLabel("Welcome to the Dice Simulator!", window)
welcome_label.setFont(QtGui.QFont("Helvetica", 16))
layout.addWidget(welcome_label)

# Result label to display the die face
result_label = QtWidgets.QLabel("⚀", window)
result_label.setFont(QtGui.QFont("Helvetica", 100))
result_label.setAlignment(QtCore.Qt.AlignCenter)
layout.addWidget(result_label)

# Roll button
roll_button = QtWidgets.QPushButton("Roll Dice", window)
roll_button.setFont(QtGui.QFont("Helvetica", 12))
roll_button.clicked.connect(roll)
layout.addWidget(roll_button)

# Exit button
exit_button = QtWidgets.QPushButton("Exit", window)
exit_button.setFont(QtGui.QFont("Helvetica", 12))
exit_button.clicked.connect(close_app)
layout.addWidget(exit_button)

# Log text box to display roll history
log_text = QtWidgets.QTextEdit(window)
log_text.setFont(QtGui.QFont("Helvetica", 10))
log_text.setReadOnly(True)
layout.addWidget(log_text)

# Set layout and show window
window.setLayout(layout)
window.show()

# Execute the application
sys.exit(app.exec_())
