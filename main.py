import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTextEdit, QLabel
from lex import lexer
from parser_1 import parser

class SimpleCompiler(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.codeInput = QTextEdit(self)
        self.layout.addWidget(QLabel('Input Code:'))
        self.layout.addWidget(self.codeInput)

        self.compileButton = QPushButton('Compile', self)
        self.compileButton.clicked.connect(self.compileCode)
        self.layout.addWidget(self.compileButton)

        self.outputLabel = QLabel('Output:', self)
        self.layout.addWidget(self.outputLabel)

        self.setLayout(self.layout)
        self.setWindowTitle('Simple Compiler')
        self.show()

    def compileCode(self):
        input_code = self.codeInput.toPlainText()
        machine_code = self.simple_compile(input_code)
        self.outputLabel.setText(f'Output:\n{machine_code}')

    def simple_compile(self, code):
        lexer.input(code)
        tokens = list(lexer)
        ast = parser.parse(code)

        registers = {}
        register_count = 0

        def allocate_register(var):
            nonlocal register_count
            if var not in registers:
                registers[var] = f'R{register_count}'
                register_count += 1
            return registers[var]

        def generate_code(node):
            if isinstance(node, tuple):
                if node[0] == 'program':
                    return '\n'.join(generate_code(n) for n in node[1])
                elif node[0] == 'declare':
                    reg = allocate_register(node[1])
                    return f'{node[1]} -> {reg}'
                elif node[0] == 'assign':
                    reg = allocate_register(node[1])
                    expr_code = generate_code(node[2])
                    return f'{expr_code}\nSTORE {reg}'
                elif node[0] in ('+', '-', '*', '/'):
                    left = generate_code(node[1])
                    right = generate_code(node[2])
                    op = {'+': 'ADD', '-': 'SUB', '*': 'MUL', '/': 'DIV'}[node[0]]
                    return f'{left}\n{right}\n{op} {allocate_register(node[1])} {allocate_register(node[2])}'
            elif isinstance(node, int):
                return f'LOADI {node}'
            elif isinstance(node, str):
                return f'LOAD {allocate_register(node)}'

        machine_code = generate_code(ast)
        return machine_code

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SimpleCompiler()
    sys.exit(app.exec_())
