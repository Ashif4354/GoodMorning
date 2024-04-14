from time import sleep
from src.WhatsApp import WhatsApp
from src.Discord import Discord
from csv import reader
from datetime import datetime
from os import getenv, system
from requests import post


def main():

    with open('data.csv', 'r', encoding='utf-8-sig') as file:
        data = list(reader(file))[1:]
        Discord().notify_dev(data)

    while True:
        time_now = datetime.now().time().strftime('%H:%M:%S')
        if time_now == getenv('DEFAULT_TIME'):
            break

    WA = WhatsApp()            

    for item in data:
        if item[1].lower() == 'text':
            WA.send_message_to_chat(item[0], item[2], item[3], int(item[4]))
        elif item[1].lower() == 'image':
            WA.send_image_to_chat(item[0], item[2], item[3], int(item[4]))
        else:
            pass

    sleep(20)


if __name__ == '__main__':
    print('STARTED THE PROCESS')
    print('WAITING ULTIL {} HRS TO PROCEED FURTHER'.format(getenv('DEFAULT_TIME')))
    main()

    system('cls')
    input('PROCESS FINISHED')

    
