from time import sleep
from src.WhatsApp import WhatsApp
from src.Discord import Discord
from csv import reader
from datetime import datetime
from os import getenv, system
from src.Time import wait


def main():

    with open('data.csv', 'r', encoding='utf-8-sig') as file:
        data = list(reader(file))[1:]
        Discord().notify_dev(data)
    
    start_time = data[0][5]
    print('WAITING UNTIL {} HRS TO PROCEED FURTHER'.format(start_time))
    while True:
        time_now = datetime.now().time().strftime('%H:%M:%S')
        if time_now >= start_time:
            break

    WA = WhatsApp()            

    for item in data:
        if item[1].lower() == 'text':
            wait(item[5])
            try:
                count= int(item[4])
            except:
                count = 1
            WA.send_message_to_chat(item[0], item[2], item[3], count)
        elif item[1].lower() == 'image':
            wait(item[5])
            try:
                count= int(item[4])
            except:
                count = 1
            WA.send_image_to_chat(item[0], item[2], item[3], count)
        else:
            pass

    sleep(20)


if __name__ == '__main__':
    print('STARTED THE PROCESS')
    main()

    system('cls')
    input('PROCESS FINISHED')

    
