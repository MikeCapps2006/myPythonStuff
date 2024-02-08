import datetime

t = datetime.time(4, 20, 1) #hours, minutes, seconds

print(t)

today = datetime.date.today() #todays date
print(today)
today2 = today.replace(year=2020) #replace year
print(today2)

print(today - today2) #outputs days between