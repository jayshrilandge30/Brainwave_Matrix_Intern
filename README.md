# Brainwave_Matrix_Intern


#Task 1- fully functional ATM interface

## Project Description

This project simulates a realistic ATM interface using Python and Tkinter, providing users with an interactive graphical user interface (GUI) to perform essential banking operations. The simulation includes various functionalities commonly found in ATMs, allowing users to select their account type, check their balance, withdraw money, and change their PIN.

## Features

- **Account Type Selection**: Users can choose their account type at the start of the interface.
- **Balance Inquiry**: View the current balance available in the account.
- **Withdrawal: Withdraw a specified amount from the account.
- Change PIN: Update the existing PIN to enhance account security.

## In-depth Explanation

The ATM Simulation is built using Python's Tkinter library, creating a user-friendly GUI.

1. Account Type Selection:
   - When the program runs, a GUI window appears prompting users to "Select your account type."
   - Upon selection, the current window disappears, and a new window prompts users to "Enter your PIN."

2. PIN Entry:
   - Users can enter their PIN and press 'ENTER' to proceed. 
   - A new window will open with the options: 
     - 1. WITHDRAWAL
     - 2. BALANCE INQ
     - 3. CHANGE PIN
     - 4. EXIT
   - The 'EXIT' option allows users to return to the previous window.

### Functionalities

#### 1. Withdrawal
- When the **WITHDRAWAL** option is selected, a new window prompts the user to "Please enter amount."
- Users can enter the desired amount and press 'ENTER' to proceed or 'CLEAR' to erase the input.
- Upon confirming, another window displays the transaction information and asks whether to show the balance.

#### 2. Balance Inquiry
- Selecting **BALANCE INQ** opens a window displaying the current balance available in the account.

#### 3. Change PIN
- Choosing **CHANGE PIN** prompts the user to enter a new PIN for their account.

#### 4. Exit
- Pressing **EXIT** returns the user to the PIN entry window.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/jayshrilandge30/atm-simulation.git
   cd atm-simulation
   ```

2. Run the ATM simulation:
   ```bash
   python atm_simulation.py
   ```

## Usage

- Launch the ATM simulation to interact with the GUI.
- Follow the prompts to perform various transactions as per the available options.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- Thanks to the Python and Tkinter documentation for providing guidance on GUI development.

---

Feel free to adjust any part of this description to better fit your style or to add more details as necessary!
