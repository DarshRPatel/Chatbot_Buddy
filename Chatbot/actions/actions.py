# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

import pymysql.cursors
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Hello World!")

        return []

class ActionCourseProf(Action):

    def name(self) -> Text:
        return "action_course_prof"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        coursename = tracker.get_slot('coursenameF') + " " + tracker.get_slot('coursenameS')

        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='qwerty',
                                    database='timetable',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

        with connection:
            with connection.cursor() as cursor:
                sql = "select distinct(profName) from instnames where insID in (select profid from instructors where \
                comcod = (select comcod from course where courseName='{}'))".format(coursename)
                cursor.execute(sql)
                result = str(cursor.fetchall())

        dispatcher.utter_message(text=result)

        return []

class ActionCreditForCourse(Action):

    def name(self) -> Text:
        return "action_credits_for_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        coursename = tracker.get_slot('coursenameF') + " " + tracker.get_slot('coursenameS')

        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='qwerty',
                                    database='timetable',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

        with connection:
            with connection.cursor() as cursor:
                sql = "select credit from course where courseName='{}'".format(coursename)
                cursor.execute(sql)
                result = str(cursor.fetchall())

        dispatcher.utter_message(text=result)

        return []

class ActionRoomForCourse(Action):

    def name(self) -> Text:
        return "action_room_for_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        coursename = tracker.get_slot('coursenameF') + " " + tracker.get_slot('coursenameS')
        section = tracker.get_slot('section')

        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='qwerty',
                                    database='timetable',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

        with connection:
            with connection.cursor() as cursor:
                sql = "select room from schedule where comcod = (select comcod from course where courseName='{}') and section like '{}%'".format(coursename, section)
                cursor.execute(sql)
                result = str(cursor.fetchall())

        dispatcher.utter_message(text=result)

        return []

class ActionCompreForCourse(Action):

    def name(self) -> Text:
        return "action_compre_for_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        coursename = tracker.get_slot('coursenameF') + " " + tracker.get_slot('coursenameS')

        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='qwerty',
                                    database='timetable',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

        with connection:
            with connection.cursor() as cursor:
                sql = "select compre from course where courseName='{}'".format(coursename)
                cursor.execute(sql)
                result = str(cursor.fetchall())

        dispatcher.utter_message(text=result)

        return []

class ActionDepartmentForCourse(Action):

    def name(self) -> Text:
        return "action_courses_under_department"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        coursenameF = tracker.get_slot('coursenameF')

        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='qwerty',
                                    database='timetable',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

        with connection:
            with connection.cursor() as cursor:
                sql = "select courseTitle from course where Upper(courseName) like Upper('{}%')".format(coursenameF)
                cursor.execute(sql)
                result = str(cursor.fetchall())

        dispatcher.utter_message(text=result)

        return []

class ActionIDForCourse(Action):

    def name(self) -> Text:
        return "action_courseid_for_course"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        coursetitle = tracker.get_slot('coursetitle')

        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='qwerty',
                                    database='timetable',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)

        with connection:
            with connection.cursor() as cursor:
                sql = "select courseName from course where courseTitle=Upper('{}')".format(coursetitle)
                cursor.execute(sql)
                result = str(cursor.fetchall())

        dispatcher.utter_message(text=result)

        return []

