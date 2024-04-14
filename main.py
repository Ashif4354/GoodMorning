from time import sleep
from src.WhatsApp import WhatsApp
from csv import reader
from datetime import datetime
from os import getenv

def main():

    while True:
        time_now = datetime.now().time().strftime('%H:%M:%S')
        if time_now == getenv('DEFAULT_TIME'):
            break


    WA = WhatsApp()

    with open('data.csv', 'r', encoding='utf-8-sig') as file:
        data = list(reader(file))[1:]

    for item in data:
        if item[1].lower() == 'text':
            WA.send_message_to_chat(item[0], item[2], item[3], int(item[4]))
        elif item[1].lower() == 'image':
            WA.send_image_to_chat(item[0], item[2], item[3], int(item[4]))
        else:
            pass

    sleep(100)


if __name__ == '__main__':
    print('STARTED THE PROCESS')
    print('WAITING ULTIL {} HRS TO PROCEED FURTHER'.format(getenv('DEFAULT_TIME')))
    main()
    # print(datetime.now().time().strftime('%H:%M'))
    
