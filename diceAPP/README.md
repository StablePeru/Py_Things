# Dice Simulator - diceApp.py

## Overview

diceApp.py is a simple yet engaging dice simulator application built using Python and PyQt5. It allows users to roll a virtual six-sided die and see the results displayed in a user-friendly interface. This application also keeps a log of the roll history with timestamps, providing a fun and interactive experience.

## Features

- **Animated Dice Roll**: Provides a short animation of rolling dice before displaying the result.
- **User-Friendly Interface**: Built with PyQt5 for an interactive and appealing graphical user interface.
- **Roll History Log**: Displays the history of rolls, including the time and result of each roll.
- **Easy Navigation**: Includes buttons for rolling the dice and exiting the application.

## Requirements

- Python 3.x
- PyQt5

You can install the dependencies using pip:

```sh
pip install PyQt5
```

## How to Run

1. Make sure you have Python 3.x and PyQt5 installed.
2. Download or clone this repository.
3. Run the script using the command line:

```sh
python diceApp.py
```

## Usage

- **Roll the Dice**: Click on the "Roll Dice" button to roll the die. The result will be displayed as a die face, and the roll history will be logged below.
- **Exit the Application**: Click on the "Exit" button to close the application.

## File Structure

- `diceApp.py`: The main Python script containing the dice simulator application logic.

## Code Overview

- **roll_dice()**: Generates a random number between 1 and 6.
- **animate_dice()**: Animates the dice roll to provide a visual effect before showing the final result.
- **display_dice()**: Displays the appropriate die face based on the roll result.
- **log_result()**: Logs the roll result with a timestamp in the log widget.

## Screenshot

(Include a screenshot of the application here if available)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests to improve the application.

## Contact

If you have any questions or suggestions, feel free to reach out.

