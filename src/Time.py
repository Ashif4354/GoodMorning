from datetime import datetime   

def wait(time):
    while True:
        time_now = datetime.now().time().strftime('%H:%M')
        if time_now == time:
            break