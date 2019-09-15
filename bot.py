import requests
import json
import datetime
import dateutil.parser
import env_secrets
import os
from timetable_headers import current, headers

link = os.environ.get("TimetableUrl")
r = requests.post(link, json=current, headers=headers)
print(r.text)