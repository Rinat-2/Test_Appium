from appium import webdriver

from pages.HomePage import HomePageHelper


class Application:
    def __init__(self):
        capabilities = {
            "deviceName": "android",
            "browserVersion": "6.0",
            "app": "https://storage.evozi.com/apk/dl/16/09/04/org.wikipedia_50377.apk",
            "appPackage": "org.wikipedia",
            "appActivity": "org.wikipedia.main.MainActivity",
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": False
            }
        }

        driver = webdriver.Remote(
            command_executor='http://159.223.108.15:4444/wd/hub',
            desired_capabilities=capabilities)
        self.driver = driver
        self.driver.launch_app()
        self.driver.implicitly_wait(10)
        self.home_page = HomePageHelper(self)

    def destroy(self):
        self.driver.remove_app('Wikipedia')
        self.driver.install_app("https://storage.evozi.com/apk/dl/16/09/04/org.wikipedia_50377.apk")
