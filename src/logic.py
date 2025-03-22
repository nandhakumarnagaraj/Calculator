import ast


class CalculatorLogic:
    @staticmethod
    def evaluate_expression(expression: str) -> str:
        try:
            return str(ast.literal_eval(expression))
        except (SyntaxError, ValueError, ZeroDivisionError):
            return "Error"
