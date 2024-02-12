import csv

f = open('find_the_link.csv', 'r')

csv_reader = csv.reader(f)

n = 0
string = []
for line in csv_reader:
    string.append(line[n])
    n += 1

google_drive_link = ''.join(string)
print(google_drive_link)

#https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q
#https://drive.google.com/open?id=1G6SEgg018UB4_4xsAJJ5TdzrhmXipr4Q
