from PySide6.QtWidgets import QVBoxLayout, QWidget, QLineEdit, QPushButton, QGridLayout


class CalculatorUI(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.grid_layout = QGridLayout()

        self.entry = QLineEdit()
        self.entry.setReadOnly(True)
        self.entry.setFixedHeight(50)
        self.layout.addWidget(self.entry)

        self.buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3),
        ]

        self.buttons_dict = {}
        for text, row, col in self.buttons:
            button = QPushButton(text)
            button.setMinimumSize(60, 60)
            self.grid_layout.addWidget(button, row, col)
            self.buttons_dict[text] = button

        self.layout.addLayout(self.grid_layout)
        self.setLayout(self.layout)
