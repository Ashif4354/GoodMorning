from time import sleep
from src.WhatsApp import WhatsApp
from src.Discord import Discord
from csv import reader
from datetime import datetime
from os import system
from src.Time import wait, get_one_minute_before


def main():

    with open('data.csv', 'r', encoding='utf-8-sig') as file:
        data = list(reader(file))[1:]
        Discord().notify_dev(data)
    
    message_start_time = input("Enter START time in 24 hour format (HH:MM:SS):")
    print('WAITING UNTIL {} HRS TO PROCEED FURTHER'.format(message_start_time))

    whats_app_start_time = get_one_minute_before(message_start_time)

    while True:
        time_now = datetime.now().time().strftime('%H:%M:%S')
        print(time_now)
        if time_now == whats_app_start_time:
            break
    WA = WhatsApp()            

    while True:
        time_now = datetime.now().time().strftime('%H:%M:%S')
        print(time_now)
        if time_now == message_start_time:
            break


    for item in data:
        if item[1].lower() == 'text':
            # wait(item[5])
            try:
                count= int(item[4])
            except:
                count = 1
            WA.send_message_to_chat(item[0], item[2], item[3], count)
        elif item[1].lower() == 'image':
            # wait(item[5])
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

    
