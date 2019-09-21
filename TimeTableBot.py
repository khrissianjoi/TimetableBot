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
    '''collects all the lectures in that week'''
    response = timetableRequest()
    lecturesOfTheWeek = json.loads(response.text)[0]['CategoryEvents']
    allLectureStartTime = []
    lecturesDetails = {}
    for lecture in lecturesOfTheWeek:
        venue = lecture['Location']
        lectureDateTime = datetime.datetime.strptime(lecture['StartDateTime'], '%Y-%m-%dT%H:%M:%S%z')
        allLectureStartTime.append(lectureDateTime)
        lecturesDetails[lectureDateTime] = lecture['ExtraProperties'][0]['Value'], venue

    return closestModuleIdentifier(lecturesDetails, allLectureStartTime)


def closestModuleIdentifier(modulesInformation, startDateTimes):
    CurrentTime = datetime.datetime.strptime("2019-09-24T09:00:00+00:00", '%Y-%m-%dT%H:%M:%S%z')
    differences = [abs(CurrentTime - each_date) for each_date in startDateTimes]
    closestDate = startDateTimes[differences.index(min(differences))]

    return modulesInformation[closestDate]

print(modulesCollector())
