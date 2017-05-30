from appium import webdriver

from core import parameters


class Driver(object):
    """
    Класс для работы с драйвером
    """

    def __init__(self):
        """
        Конструктор класса
        """
        self.host = parameters.host
        self.port = parameters.port
        self.desired_capabilities = {'platformName': parameters.platformName,
                                     'platformVersion': parameters.platformVersion,
                                     'deviceName': parameters.deviceName,
                                     'appPackage': parameters.appPackage,
                                     'appActivity': parameters.appActivity}
        self.driver = None

    def init_driver(self):
        """
        Метод инициализации объекта вебдрайвера

        :return: Объект вебдрайвера
        """
        self.driver = webdriver.Remote(command_executor='http://{0}:{1}/wd/hub'.format(self.host, self.port),
                                       desired_capabilities=self.desired_capabilities)
        return self.driver

