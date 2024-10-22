# Password Generator Application

A simple, user-friendly password generator built using PyQt5 and Python. This application allows users to generate secure passwords with customizable options and save them to an Excel file for future reference. It also features an easy-to-use interface for viewing, copying, and managing saved passwords.

## Features

- **Password Generation**: Generate strong passwords with customizable options, including uppercase letters, numbers, and symbols.
- **Save Passwords**: Save generated passwords along with website/app names and usernames in an Excel file.
- **View Saved Passwords**: View previously saved passwords in a tabular format.
- **Password Visibility**: Toggle password visibility for easier management.
- **Copy to Clipboard**: Easily copy passwords to the clipboard for use.
- **Responsive Design**: User-friendly interface with readable fonts and an organized layout.

## Technologies Used

- **Python**: Core programming language used for this application.
- **PyQt5**: GUI toolkit used to create the application's user interface.
- **OpenPyXL**: Library used for working with Excel files to store saved passwords.
- **Pyperclip**: Library used to copy passwords to the clipboard.

## Installation

### 1. Clone the Repository

Clone the repository:

```sh
git clone https://github.com/StablePeru/Py_Things/tree/main/PassGenerator.git
```

Change directory to the project folder:

```sh
cd password-generator-app
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
python password_generator.py
```

## Usage

- **Generate a Password**: Enter the desired password length and select the options you need (uppercase letters, numbers, symbols), then click "Generate Password".
- **Save a Password**: Fill in the website/app name, username, and the generated password, then click "Save Password" to store it in an Excel file (`passwords.xlsx`).
- **View Saved Passwords**: Click "Show Saved Passwords" to see previously saved passwords in a table format. You can also copy any password by clicking on it.

## Screenshots

### Main Interface

(Include a screenshot of the main interface here.)

### Saved Passwords

(Include a screenshot of the saved passwords table here.)

## Requirements

- Python 3.6+
- PyQt5
- OpenPyXL
- Pyperclip

You can install the required packages using the following command:

```sh
pip install PyQt5 openpyxl pyperclip
```

## Contributing

Contributions are welcome! If you have any improvements or suggestions, feel free to fork the repository, make your changes, and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Author

- **StablePeru** - [GitHub Profile](https://github.com/StablePeru)

Feel free to reach out with any questions or suggestions regarding this project!

