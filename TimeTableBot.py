import datetime
import json
import os
import requests

import env_secrets
from TimetableHeaders import current, headers


def timetableRequest():
    link = os.environ.get("TimetableUrl")
    response = requests.post(link, json=current, headers=headers)
    return response


def modulesCollector():
    response = timetableRequest()
    modules = json.loads(response.text)[0]['CategoryEvents']
    time = datetime.datetime.today()
    times = {}
    dates = []
    for module in modules:
        venue = module['Location']
        time = datetime.datetime.strptime(module['StartDateTime'], '%Y-%m-%dT%H:%M:%S%z')
        dates.append(time)
        times[time] = module['ExtraProperties'][0]['Value'], venue

    return closestModuleIdentifier(times, dates)


def closestModuleIdentifier(modulesInformation, startDateTimes):
    CurrentTime = datetime.datetime.strptime("2019-09-24T09:00:00+00:00", '%Y-%m-%dT%H:%M:%S%z')
    differences = [abs(CurrentTime - each_date) for each_date in startDateTimes]
    closestDate = startDateTimes[differences.index(min(differences))]
    
    return modulesInformation[closestDate]

print(modulesCollector())