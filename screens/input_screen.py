from appium import webdriver


class InputScreen(object):
    """
    Класс экрана ввода приложения
    """

    def __init__(self, driver: webdriver, value: str):
        """
        Конструктор класса

        :param driver: Объект вебдрайвера
        :param value: Число для расчета факториала
        """
        self.driver = driver
        self.value = value

    def input_value(self):
        """
        Вводим число в поле ввода
        """
        self.driver.find_element_by_id('interview.factorial:id/text_input').send_keys(self.value)

    def click_button(self):
        """
        Нажимаем на кнопку "Рассчитать факториал"
        """
        self.driver.find_element_by_id('interview.factorial:id/fab').click()
