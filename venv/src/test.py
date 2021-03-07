from pyexcel_xlsx import get_data
from bson import json_util
import json

data = get_data("output2.xlsx")
"""
dataprinting = json.dumps(data, indent=4, default=json_util.default)
print(datapriting)
"""

alldata = data["Formularantworten 1"]
dataset = alldata[1]

# Filling factor-IDs:

owndatadict = dict()
owndatadict[dataset[1]] = {}
owndatadict[dataset[1]]["date"] = dataset[1]
owndatadict[dataset[1]]["hoehepunkt_kopfschmerz"] = dataset[2]
owndatadict[dataset[1]]["durchschnitt_kopfschmerz"] = dataset[3]
owndatadict[dataset[1]]["hoehepunkt_nackenschmerz"] = dataset[4]
owndatadict[dataset[1]]["durchschnitt_nackenschmerz"] = dataset[5]
owndatadict[dataset[1]]["durchschnitt_stresspiegel"] = dataset[6]
owndatadict[dataset[1]]["durchschnitt_gesamtstimmung"] = dataset[7]
owndatadict[dataset[1]]["wetter"] = dataset[8]
owndatadict[dataset[1]]["hoechsttemperatur"] = dataset[9]
owndatadict[dataset[1]]["zeit_aussen"] = dataset[10]
owndatadict[dataset[1]]["sport"] = dataset[11]
owndatadict[dataset[1]]["getrunken"] = dataset[12]
owndatadict[dataset[1]]["medikamente"] = dataset[13]

# check if Anmerkung field is filled, if yes, add to owndatadict
if 14 in dataset:
    owndatadict[dataset[1]]["anmerkung"] = dataset[14]

import pdb; pdb.set_trace()