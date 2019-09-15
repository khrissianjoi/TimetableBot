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
    "ac1c8470-e74f-5239-c153-ccc42c836613"
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