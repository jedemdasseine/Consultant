from core.driver import Driver
from screens.input_screen import InputScreen
from screens.result_screen import ResultScreen


def memorize(func):
    """
    Декоратор, отдающий объект, если он был уже инициализирован

    :param func: Функция
    :return: Враппер
    """
    def wrapper(self):
        """
        Враппер для получения имени атрибута
        :param self: Объект
        :return: Имя атрибута
        """
        store_attr_name = '_{0}'.format(func.__name__)
        if not hasattr(self, store_attr_name):
            setattr(self, store_attr_name, func(self))
        return getattr(self, store_attr_name)
    return wrapper


class Application(object):
    """
    Класс приложения для работы с объектами экранов и драйвера
    """

    def __init__(self, value: str):
        """
        Конструктор класса

        :param value: Число для расчета факториала
        """
        self.value = value

    @memorize
    def driver(self):
        """
        Метод для инициализации объекта драйвера

        :return: Объект драйвера
        """
        return Driver().init_driver()

    @memorize
    def input_screen(self):
        """
        Метод для инициализации объекта экрана ввода

        :return: Объект экрана ввода
        """
        return InputScreen(self.driver(), self.value)

    @memorize
    def result_screen(self):
        """
        Метод для инициализации объекта экрана результата

        :return: Объект экрана результата
        """
        return ResultScreen(self.driver())
