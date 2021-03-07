from pyexcel_xlsx import get_data#
from bson import json_util
import json

data = get_data("output2.xlsx")
"""
dataprinting = json.dumps(data, indent=4, default=json_util.default)
print(datapriting)
"""

alldata = data["Formularantworten 1"]
print(alldata[1])

# Filling factor-IDs:

owndatadict = dict()
#owndatadict[date]
#owndatadict[date]["wetter"]
#owndatadict[date]["durchschnitt_stresspiegel"]
#owndatadict[date]["durchschnitt_gesamtstimmung"]
#owndatadict[date]["hoehepunkt_kopfschmerz"]
#owndatadict[date]["durchschnitt_kopfschmerz"]
#owndatadict[date]["getrunken"]
#owndatadict[date]["hoechsttemperatur"]
#owndatadict[date]["zeit_aussen"]

#import pdb; pdb.set_trace()