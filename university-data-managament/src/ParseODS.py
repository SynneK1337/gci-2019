from pyexcel_ods import get_data
import json


class ParseODS():
    def __init__(self, filename):
        self.doc = get_data(filename)
        self.data = json.loads(json.dumps(self.doc))["Sheet1"]
        self.subjects = self.data[2]

    def get_students_names(self):
        students = []
        for student in self.data[3:]:
            if student:
                students.append(student[0])
        return students

    def get_student(self, name):
        student_ = {"name": name}
        for student in self.data[3:]:
            if student[0] == name:
                for score in student[1:]:
                    student_[self.subjects[student.index(score)]] = score
                break
        return student_

    def get_avarage(self, name):
        avarage = 0
        divider = 0
        for student in self.data[3:]:
            if student[0] == name:
                for score in student[1:]:
                    if self.subjects[student.index(score)] == "Physics" or self.subjects[student.index(
                            score)] == "Geometry" or self.subjects[student.index(score)] == "Algebra":
                        avarage += score * 2
                        divider += 2
                    else:
                        avarage += score
                        divider += 1
                break
        return avarage / divider

