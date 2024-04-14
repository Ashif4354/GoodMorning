import csv

with open('data.csv', 'r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    print(list(reader))