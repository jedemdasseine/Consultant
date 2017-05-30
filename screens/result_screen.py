from appium import webdriver


class ResultScreen(object):
    """
    Класс экрана результата приложения
    """

    def __init__(self, driver: webdriver):
        """
        Конструктор класса

        :param driver: Объект вебдрайвера
        """
        self.driver = driver

    def get_result_value(self):
        """
        Получаем результат вычисления факториала приложением

        :return: Результат вычисления факториала
        """
        return self.driver.find_element_by_id('interview.factorial:id/text_output').text
