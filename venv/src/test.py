from pyexcel_xlsx import get_data#
from bson import json_util
import json

data = get_data("output2.xlsx")
dataprinting = json.dumps(data, indent=4, default=json_util.default)

print(dataprinting)