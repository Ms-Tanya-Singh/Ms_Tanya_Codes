# Simple Python Expression Calculator

This project is a command-line calculator written in Python. It allows users to enter simple arithmetic expressions involving two operands and one binary operator. The program processes the expression, evaluates it, and displays the result. It runs in a loop until the user chooses to exit.

## Features

- Supports the following operators:
  - `+` (Addition)
  - `-` (Subtraction)
  - `*` (Multiplication)
  - `/` (Division)
  - `%` (Modulus)
  - `**` (Exponentiation)
  - `//` (Floor Division)
- Handles whitespace in expressions (e.g., `5  +  3`)
- Uses structured exception handling (`try/except`) for robust input validation
- Detects and reports invalid expressions or number formats
- Prevents division by zero
- Continues prompting the user until `q` or `quit` is entered

## Requirements

- Python 3.x

## How to Run

1. Clone or download the repository.
2. Run the script using Python:

```bash
python calculator.py
```

3. Follow the prompt (example):

```text
Enter expression: 10 + 5
10.0 + 5.0 = 15.0

Enter expression: 4 ** 3
4.0 ** 3.0 = 64.0

Enter expression: quit
Goodbye!
```

## Code Overview

- Operator functions (`add`, `subtract`, `multiply`, etc.) are defined separately.
- A dictionary maps operator symbols to the corresponding functions.
- The input string is stripped and parsed using `.split(op)` to extract operands.
- The input loop allows continuous use until explicitly terminated.

## License

This project is open source and available under the MIT License.
