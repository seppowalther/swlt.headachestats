import datetime
from pandas_ods_reader import read_ods

# defining data output path
path = "output.ods"
record = read_ods(path, 1)

for column in record['Datensatz für folgenden Tag:']:
    print(column)

# Datensatz-Aufbereitung

tableoutput = "24.02.2021 20:39:22"
splittet = tableoutput.split('.')

day = splittet[0]
month = splittet[1]
year = (splittet[2].split(' '))[0]

date = datetime.datetime(int(year), int(month), int(day))

# Faktoren-IDs:

date = date
hoehepunkt_kopfschmerz = 0
durchschnitt_kopfschmerz = 0
hoehepunkt_nackenschmerzen = 0
durchschnitt_nackenschmerzen = 0
durchschnitt_stresspiegel = 0
durchschnitt_gesamtstimmung = 0
wetter = ['sonnig','bewoelkt','regnerisch','neblig']
hoechsttemperatur = ['>35', '30-35', '20-30', '10-20', '5-10', '0-5', '<0']
zeit_aussen = ['>3', '>2', '>1', '0-1', '0']
sport = ['indoor', 'outdoor', 'no']
getrunken = ['>3,5', '2,5-3,5', '2-2,5', '<2']
medikamente = ['ibuprofen', 'paracetamol', 'aspirin', 'neuralgin']

#

print(date)