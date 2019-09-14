import requests
import json
import datetime
import dateutil.parser
import env_secrets
import os
import datetime


# my_time = datetime.datetime.now().isoformat()
my_time = "2019-09-23T14:17:45.412370Z"
current = {
  "ViewOptions": {
    "Weeks": [
      {
        "FirstDayInWeek": my_time
      }
    ]
  },
  "CategoryIdentities": [
    "38b55ac0-a242-23d3-4a10-79f11bdd780c"
  ]
}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'basic T64Mdy7m['
}


time_module = {}

link = os.environ.get("TimetableUrl")
r = requests.post(link, json=current, headers=headers)
print(r.text)