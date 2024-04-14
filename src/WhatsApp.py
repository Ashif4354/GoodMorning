from .Selenium import Selenium
from .CopyImage import copy_to_clipboard
from time import sleep


class WhatsApp(Selenium):
    def __init__(self):
        super().__init__()
        self.open_whats_app()

    def open_whats_app(self):
        self.browser.get('https://web.whatsapp.com/')
        
    def find_chat(self, name):
        try:
            cancel_search_xpath = '//button[@aria-label="Cancel search"]'
            self.find_and_click_element(cancel_search_xpath)
        except:
            pass

        text_box_xpath = '//div[@title="Search input textbox"]'
        self.clear_text_box(text_box_xpath)
        self.type(text_box_xpath, name)

    def type_message(self, message):
        text_box_xpath = '//div[@title="Type a message"]'
        self.type(text_box_xpath, message)

    def send_message_to_chat(self, name, message, caption, count):
        self.find_chat(name)
        
        for i in range(count):
            self.type_message(message + caption)
            sleep(.5)

    def send_image_to_chat(self, name, image_path, caption, count):
        self.find_chat(name)

        for i in range(count):
            copy_to_clipboard(image_path)
            self.paste()
            sleep(.5)
            self.type_message(caption)
            self.print_logs('Image sent')
            sleep(.5)

if __name__ == '__main__':
    w = WhatsApp()
    w.open_whats_app()

    w.find_and_click_element('//button[@aria-label="Search or start new chat"]')
    w.type('//div[@title="Search input textbox"]', 'Afthab')
    sleep(100)