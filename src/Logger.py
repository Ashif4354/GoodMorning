from os import getenv

class Logger:
    def __init__(self):
        pass

    def print_logs(self, *texts):
        if getenv('print_logs') == 'TRUE':
            print(*texts)   