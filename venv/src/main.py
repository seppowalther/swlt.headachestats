import datetime

# ODS-Output Format
"""
from pandas_ods_reader import read_ods
path = "output.ods"
record = read_ods(path, 1)

for column in record['Datensatz für folgenden Tag:']:
    print(column)
"""

# CSV-Output Format
import csv
testlist = []
with open('output.csv', newline='') as csvfile:
    test = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in test:
        testlist.append(', '.join(row))

testlist_splitted = testlist[3].split(',')


# Datums-Aufbereitung

tableoutput = testlist_splitted[5]
splittet = tableoutput.split('.')

day = splittet[0]
month = splittet[1]
year = splittet[2]
date = datetime.datetime(int(year), int(month), int(day))

"""
AVAILABLE factor-IDs:

wetter = ['sonnig','bewoelkt','regnerisch','neblig']
hoechsttemperatur = ['>35', '30-35', '20-30', '10-20', '5-10', '0-5', '<0']
zeit_aussen = ['>3', '>2', '>1', '0-1', '0']
sport = ['indoor', 'outdoor', 'no']
getrunken = ['>3,5', '2,5-3,5', '2-2,5', '<2']
medikamente = ['ibuprofen', 'paracetamol', 'aspirin', 'neuralgin']
"""

# Preparing CSV-Output-factors for further data processing

# Preparing wetter
if testlist_splitted[2] == "Sonnig":
    wetter = 'sonnig'
elif testlist_splitted[2] == "Bewölkt":
    wetter = 'bewoelkt'
elif testlist_splitted[2] == "Regnerisch":
    wetter = 'regnerisch'
elif testlist_splitted[2] == "Neblig":
    wetter = 'neblig'

# Preparing getrunken
if testlist_splitted[9] == '"Mehr':
    getrunken = '>3,5'
elif testlist_splitted[9] == '"Genug':
    getrunken = '2,5-3,5'
elif testlist_splitted[9] == '"Etwas':
    getrunken = '2-2,5'
elif testlist_splitted[9] == '"Viel':
    getrunken = '<2'

# Filling factor-IDs:
date = date
wetter = wetter
getrunken = getrunken
hoehepunkt_kopfschmerz = 0
durchschnitt_kopfschmerz = 0
hoehepunkt_nackenschmerzen = 0
durchschnitt_nackenschmerzen = 0
durchschnitt_stresspiegel = testlist_splitted[3]
durchschnitt_gesamtstimmung = 0

owndatadict = dict()
owndatadict[date] = {}
owndatadict[date]["wetter"] = wetter
owndatadict[date]["durchschnitt_stresspiegel"] = testlist_splitted[3]

import pdb; pdb.set_trace()
