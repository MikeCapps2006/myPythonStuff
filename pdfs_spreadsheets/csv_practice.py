from csv import *

file = open('example.csv')

reader = reader(file)

data_lines = list(reader)

""" for line in data_lines[:5]:
    print(line) """

all_emails = []
for line in data_lines[1:]:
    all_emails.append(line[3])

""" for email in all_emails:
    print(email)
 """

file = open('to_save_file.csv', 'w', newline='')
csv_writer = writer(file, delimiter=',')
csv_writer.writerow(['Name', 'Email', 'Phone Number'])

csv_writer.writerows([['Mike', 'michaelcapps1772@yahoo.com', '843-999-9999'],
                     ['Josie', 'josie.camp@yahoo.com', '999-888-7654']])

file.close()