# Password Generator

This is a simple password generator built in Python. It allows users to specify the number of letters, numbers, and symbols they want to include in the generated password. The program then combines random selections from a list of letters, numbers, and symbols to create a secure password.

## Features

- Customizable password length with options for the number of letters, numbers, and symbols.
- Randomly generates characters from predefined lists of uppercase letters, lowercase letters, numbers, and symbols.
- Password characters are shuffled to ensure randomness and security.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/password-generator.git
   ```

2. Navigate into the project directory:
   ```bash
   cd password-generator
   ```

3. Make sure you have Python installed. You can download Python [here](https://www.python.org/downloads/).

4. Run the password generator script:
   ```bash
   python password_generator.py
   ```

## Usage

- When you run the script, you will be prompted to input the number of letters, numbers, and symbols you want in the password.
- The script will generate a password with your specified criteria, combining random letters, numbers, and symbols.
- The password will be printed in a random order for maximum security.

### Example

```
Enter number of letters: 5
Enter number of numbers: 3
Enter number of symbols: 2
Generated Password: b3#D@9g
```

## Code Breakdown
1. **letters**: A list of uppercase and lowercase letters.
2. **numbers**: A list of digits from 0 to 9.
3. **symbols**: A list of common special characters.
4. **User Input**: The program asks for input to specify how many letters, numbers, and symbols to include.
5. **Password Generation**: Based on the input, the program randomly selects characters from the appropriate list.
6. **Shuffling**: The generated characters are shuffled to ensure the password is random and unpredictable.
7. **Output**: The final password is printed to the console.


## Author
https://github.com/AyushTIW30/password_gen/new/main?filename=README.md

