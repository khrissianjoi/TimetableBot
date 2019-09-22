import datetime
import json
import os
import requests

import env_secrets
from TimetableHeaders import current, headers


def timetableRequest():
    '''api call to timetable'''
    link = os.environ.get("TimetableUrl")
    return requests.post(link, json=current, headers=headers)
    

def modulesCollector():
    '''collects all the lectures in cuurent week'''
    response = timetableRequest()
    lecturesOfTheWeek = json.loads(response.text)[0]['CategoryEvents']
    allLectureStartTime = []
    lecturesDetails = {}
    for lecture in lecturesOfTheWeek:
        venue = lecture['Location']
        lectureTitle = lecture['ExtraProperties'][0]['Value']
        lectureDateTime = datetime.datetime.strptime(lecture['StartDateTime'],
                                                     '%Y-%m-%dT%H:%M:%S%z')
        allLectureStartTime.append(lectureDateTime)
        lecturesDetails[lectureDateTime] = lectureTitle, venue

    return closestModuleIdentifier(lecturesDetails, allLectureStartTime)


def closestModuleIdentifier(modulesInformation, startDateTimes):
    '''calculates the next lecture by comparing with the current time'''
    currentTime = datetime.datetime.strptime("2019-09-24T09:00:00+00:00",
                                             '%Y-%m-%dT%H:%M:%S%z')
    differences = [abs(currentTime - eachDate) for eachDate in startDateTimes]
    closestDate = startDateTimes[differences.index(min(differences))]

    return modulesInformation[closestDate]


print(modulesCollector())
