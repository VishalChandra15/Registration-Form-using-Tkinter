# Registration Form with Tkinter

This is a simple GUI-based registration form created using Python's `tkinter` library. The form collects user information (Name, Email, and Age) and stores the data in a CSV file (`registration_data.csv`).

## Features
- Input fields for Name, Email, and Age.
- Validates that all fields are filled before submitting.
- Appends data to a CSV file with headers.
- Displays success or error messages via popups.

## Prerequisites

- Python 3.x

## Getting Started

1. Clone or download this repository to your local machine.
2. Install the required packages by running the following command:
    ```bash
    pip install -r requirements.txt
    ```
3. Run the script:
    ```bash
    python main.py
    ```

4. Fill in the form and click the "Submit" button. If all fields are filled, the information will be stored in `registration_data.csv`, and a success message will appear.

## File Descriptions

- **registration_form.py**: The main Python script containing the tkinter GUI and logic to submit the form.
- **registration_data.csv**: The file where user input data is stored.
- **README.md**: Project description and instructions.
- **requirements.txt**: List of dependencies required to run the project.

## Usage

- Run the `main.py` file.
- Input the required information (Name, Email, Age) and press the submit button.
- The form will check if all fields are filled and store the data in `registration_data.csv`.
- A success message will appear on successful registration, or an error message will appear if the fields are not filled.

## License

This project is open-source and available under the MIT License.
