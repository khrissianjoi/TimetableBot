import datetime
import json
import os
import requests

import env_secrets
from TimetableHeaders import current, headers


link = os.environ.get("TimetableUrl")
response = requests.post(link, json=current, headers=headers)

modules = json.loads(response.text)[0]['CategoryEvents']
time = datetime.datetime.today()
times= {}
for module in modules[::-1]:
    time = datetime.datetime.strptime(module['StartDateTime'], '%Y-%m-%dT%H:%M:%S%z')
    print(type(time))
    times[time] = module['ExtraProperties'][0]['Value']

module_pertime = list(times.keys())
print(module_pertime)