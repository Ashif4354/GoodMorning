from datetime import datetime   

def wait(time):
    while True:
        if datetime.now().time().strftime('%H:%M:%S') > time:
            return