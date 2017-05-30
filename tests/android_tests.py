import unittest

from core.application import Application
from screens import additional_methods


class FunctionalTest(unittest.TestCase):
    """
    Тестовый класс
    """

    def setUp(self):
        """
        Метод, который всегда выполняется перед тестовыми методами
        """
        # Получаем число для расчета факториала
        self.value = additional_methods.generate_input_value(10)
        # Рассчитываем факториал, для валидации результата работы приложения
        self.required_number = str(additional_methods.get_factorial(self.value))
        # Инициализируем приложение, которое управляет инциализацией объектов драйвера и экранов
        self.app = Application(self.value)

    def test_factorial(self):
        """
        Тестовый метод для проверки логики работы приложения
        """
        # Вводим число в поле ввода
        self.app.input_screen().input_value()
        # Нажимаем на кнопку расчета факториала
        self.app.input_screen().click_button()
        # Сравниваем результаты расчета факториала приложением
        self.assertEqual(self.app.result_screen().get_result_value(), self.required_number, "Incorrect result")

    def tearDown(self):
        """
        Метод, который всегда выполняется после тестовых методов
        """
        # Завершаем работу драйвера
        self.app.driver().quit()


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(FunctionalTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
