from PySide6.QtWidgets import QApplication, QMainWindow
from src.ui import CalculatorUI
from src.logic import CalculatorLogic


class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Simple Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.ui = CalculatorUI()
        self.setCentralWidget(self.ui)

        self.connect_signals()

    def connect_signals(self):
        for text, button in self.ui.buttons_dict.items():
            button.clicked.connect(lambda checked, t=text: self.on_button_click(t))

    def on_button_click(self, text):
        current_text = self.ui.entry.text()

        if text == "C":
            self.ui.entry.clear()
        elif text == "=":
            result = CalculatorLogic.evaluate_expression(current_text)
            self.ui.entry.setText(result)
        else:
            if current_text and current_text[-1] in "+-*/" and text in "+-*/":
                return
            if not current_text and text in "+*/":
                return

            self.ui.entry.setText(current_text + text)


if __name__ == "__main__":
    app = QApplication([])
    calculator = Calculator()
    calculator.show()
    app.exec()
