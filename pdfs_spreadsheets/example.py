import csv

data = open('example.csv', encoding='utf-8')

csv_data = csv.reader(data)

print(csv_data)