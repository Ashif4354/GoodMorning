from datetime import datetime   

def wait(time):
    while True:
        if datetime.now().time().strftime('%H:%M:%S') > time:
            return
        

def get_one_minute_before(time):
    time =  time.split(':')
    time = [int(i) for i in time]

    if time[1] == 0:
        time[1] = 59
        if time[0] == 0:
            time[0] = 23
        else:
            time[0] -= 1
    else:
        time[1] -= 1

    time = [str(i) for i in time]
    for i in range(len(time)):
        if len(time[i]) == 1:
            time[i] = '0' + time[i]

    time = ':'.join(time)
    return time


if __name__ == '__main__':
    print(get_one_minute_before('00:00:00'))
    print(get_one_minute_before('00:00:01'))
    print(get_one_minute_before('00:01:00'))
    print(get_one_minute_before('01:00:00'))
    print(get_one_minute_before('01:01:01'))
    print(get_one_minute_before('23:59:59'))
    