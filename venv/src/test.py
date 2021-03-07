from pyexcel_xlsx import get_data#
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
#owndatadict[dataset[1]]["durchschnitt_kopfschmerz"] = dataset[3]
#owndatadict[dataset[1]]["wetter"] =
#owndatadict[dataset[1]]["durchschnitt_stresspiegel"]
#owndatadict[dataset[1]]["durchschnitt_gesamtstimmung"]
#owndatadict[dataset[1]]["getrunken"]
#owndatadict[dataset[1]]["hoechsttemperatur"]
#owndatadict[dataset[1]]["zeit_aussen"]

import pdb; pdb.set_trace()