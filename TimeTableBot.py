import requests
import json
import datetime
import dateutil.parser
import env_secrets
import os
from timetable_headers import current, headers

link = os.environ.get("TimetableUrl")
response = requests.post(link, json=current, headers=headers)

modules = json.loads(response.text)[0]['CategoryEvents']

for module in modules[::-1]:
  print(module['ExtraProperties'][0]['Value'])

