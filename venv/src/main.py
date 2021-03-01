import datetime

# Datensatz-Aufbereitung

tableoutput = "24.02.2021 20:39:22"
splittet = tableoutput.split('.')

day = splittet[0]
month = splittet[1]
year = (splittet[2].split(' '))[0]

date = datetime.datetime(int(year), int(month), int(day))

# Faktoren-IDs:

hoehepunkt_kopfschmerz = 0
durchschnitt_kopfschmerz = 0
hoehepunkt_nackenschmerzen = 0
durchschnitt_nackenschmerzen = 0
durchschnitt_stresspiegel = 0
durchschnitt_gesamtstimmung = 0
wetter = ['sonnig','bewoelkt','regnerisch','neblig']
hoechsttemperatur = ['>35', '30-35', '20-30', '10-20', '5-10', '0-5', '<0']

import pdb; pdb.set_trace()

print(date)