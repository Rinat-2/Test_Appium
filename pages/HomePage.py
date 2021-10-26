class HomePageHelper:
    def __init__(self, app):
        self.app = app

    def reset_app(self):
        driver = self.app.driver
        driver.remove_app('Wikipedia')
        driver.install_app("https://storage.evozi.com/apk/dl/16/09/04/org.wikipedia_50377.apk")
        driver.launch_app()

    def skip_onboarding(self):
        driver = self.app.driver
        driver.find_element_by_id('org.wikipedia:id/fragment_onboarding_skip_button').click()

    def click_on_saved(self):
        driver = self.app.driver
        driver.find_element_by_accessibility_id('Saved').click()
