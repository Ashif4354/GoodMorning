from selenium.webdriver import Edge, EdgeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from .Logger import Logger
from .Discord import Discord
from os import getenv

class Selenium(Discord, Logger):
    def __init__(self):
        super().__init__()
        options = EdgeOptions()
        options.add_argument(r'user-data-dir=C:\Users\{}\AppData\Local\Microsoft\Edge\User Data'.format(getenv('USERNAME')))
        self.open_browser(options)
        self.browser_actions = ActionChains(self.browser)
        
    def open_browser(self, options):
        self.browser = Edge(options=options)
        self.browser.maximize_window()

    def find_and_click_element(self, xpath):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element = self.browser.find_element(By.XPATH, xpath)
        element.click()

    def clear_text_box(self, xpath):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
        element = self.browser.find_element(By.XPATH, xpath)
        element.clear()

    def type(self, xpath, text):
        WebDriverWait(self.browser, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
        print('Started typing', text)
        element = self.browser.find_element(By.XPATH, xpath)
        element.send_keys(text)

    def press_enter(self):
        self.browser_actions.send_keys(Keys.ENTER).perform()
    
    def paste(self):
        self.browser_actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    def end(self):
        self.browser.quit()
    

if __name__ == '__main__':
    s = Selenium()