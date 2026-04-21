class Calculator:
    """Простейший калькулятор с четырьмя арифметическими операциями."""

    def add(self, a: float, b: float) -> float:
        """Возвращает сумму a и b."""
        # TODO: реализуйте сложение
        return a + b;

    def subtract(self, a: float, b: float) -> float:
        """Возвращает разность a и b."""
        # TODO: реализуйте вычитание
        return a - b;

    def multiply(self, a: float, b: float) -> float:
        """Возвращает произведение a и b."""
        # TODO: реализуйте умножение
        return a * b;

    def divide(self, a: float, b: float) -> float:
        """Возвращает частное a и b.

        Raises:
            ValueError: если b равно нулю.
        """
        # TODO: реализуйте деление
        # Не забудьте обработать деление на ноль
        if b == 0:
            raise ValueError("Деление на ноль");
        return a / b;
