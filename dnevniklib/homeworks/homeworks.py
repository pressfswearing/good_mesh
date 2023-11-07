from dnevniklib.student import Student
from requests import get

class Homeworks:
    def __init__(self, student: Student):
        self.token = student.token
        self.student_id = student.id


    def get_homework_by_date(self, date):
        res = []
        response = get(
            f"https://school.mos.ru/api/family/web/v1/homeworks?from={date}&to={date}&student_id={self.student_id}",
            headers={
                "Auth-Token": self.token,
                "X-Mes-Subsystem": "familyweb"
            }
        )
        for homework in response.json()["payload"]:
            if 'subject_name' in homework and 'description' in homework:
                res.append(homework['subject_name'] + ': ' + homework['description'])
        return res

    def get_schedule(self, date):
        res = []
        response = get(
            f"https://school.mos.ru/api/family/web/v1/schedule?student_id={self.student_id}&date={date}",
            headers={
                "Auth-Token": self.token,
                "X-Mes-Subsystem": "familyweb"
            }
        )
        for schedule in response.json()["activities"]:
            if 'lesson' in schedule and 'subject_name' in schedule['lesson'] and 'begin_time' in schedule and 'end_time' in schedule:
                res.append(schedule['lesson']['subject_name'] + ': ' + schedule['begin_time'] + '-' + schedule['end_time'])
        return res

    def get_marks(self, date):
        res = []
        response = get(
            f"https://school.mos.ru/api/family/web/v1/schedule?student_id={self.student_id}&date={date}",
            headers={
                "Auth-Token": self.token,
                "X-Mes-Subsystem": "familyweb"
            }
        )
        for activity in response.json()["activities"]:
            if 'lesson' in activity and 'marks' in activity['lesson'] and 'subject_name' in activity['lesson']:
                for mark in activity['lesson']['marks']:
                    value = mark['value']
                    res.append(activity['lesson']['subject_name'] + ': ' + value)
        return res

    def get_trimester_marks(self, trimester, academic_year_id: int = 11):
        data = get(
            f"https://dnevnik.mos.ru/reports/api/progress/json?academic_year_id={academic_year_id}&student_profile_id={self.student_id}",
            headers={
                "Authorization": self.token,
                "Auth-Token": self.token
            }
        )
        marks = []
        for lesson in data.json():
            lesson_name = lesson["subject_name"]
            if lesson["periods"]:
                trimester_mark = lesson["periods"][0]["avg_five"]
            else:
                trimester_mark = "0"
            marks.append(
                {
                    "name": lesson_name,
                    "mark": trimester_mark
                }
            )
        return marks