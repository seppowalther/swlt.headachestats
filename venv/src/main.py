import datetime

tableoutput = "24.02.2021 20:39:22"
splittet = tableoutput.split('.')

day = splittet[0]
month = splittet[1]
year = (splittet[2].split(' '))[0]

date = datetime.datetime(int(year), int(month), int(day))

print(date)