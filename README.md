# Simple Compiler

A simple compiler implemented in Python with a GUI built using PyQt5. This project takes user input code, processes it through lexical analysis and parsing, and generates machine-like code representation.

## Features
- Lexical analysis and parsing using a custom lexer and parser.
- Generates machine-like code with register allocation.
- GUI interface for easy code input and compilation.

## Installation

### Prerequisites
Make sure you have Python installed. You also need to install PyQt5:

```bash
pip install PyQt5
```

### Clone the Repository
```bash
git clone https://github.com/alishahrouzi/Simple-Compiler.git
cd Simple-Compiler
```

## Usage
Run the compiler GUI using:
```bash
python main.py
```

### How It Works
1. Enter your code in the text input field.
2. Click the **Compile** button.
3. The output machine code will be displayed.

### Example Input
```plaintext
x = 5
y = x + 3
```

### Example Output
```plaintext
LOADI 5
STORE R0
LOAD R0
LOADI 3
ADD R0 R1
STORE R1
```

## Project Structure
```
Simple-Compiler/
│── main.py            # Main GUI application
│── lex.py             # Lexer implementation
│── parser_1.py        # Parser implementation
│── README.md          # Project documentation
```

## Lexer (lex.py)
The lexer is responsible for tokenizing the input code. It scans the input and breaks it down into tokens such as identifiers, operators, and literals. This is the first step in the compilation process.

## Parser (parser_1.py)
The parser takes the tokens produced by the lexer and constructs an Abstract Syntax Tree (AST). It ensures that the input follows the correct syntactic structure and prepares it for code generation.

## Contributing
Feel free to fork this repository and submit pull requests for improvements.

## License
This project is licensed under the MIT License.

