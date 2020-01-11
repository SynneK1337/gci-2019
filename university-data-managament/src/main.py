from ParseODS import ParseODS


def get_avarage_of_all_academics(score1, score2, score3, score4):
    avarage = 0
    divider = 0
    for subject in score1:
        if subject == "name":
            pass
        elif subject == "Algebra":
            avarage += score1[subject] * 2
            divider += 2
        elif subject == "Physics":
            avarage += score1[subject] * 2
            divider += 2
        elif subject == "Geometry":
            avarage += score1[subject] * 2
            divider += 2
        else:
            avarage += score1[subject]
            divider += 1
    for subject in score2:
        if subject == "name":
            pass
        elif subject == "Algebra":
            avarage += score2[subject] * 2
            divider += 2
        elif subject == "Physics":
            avarage += score2[subject] * 2
            divider += 2
        elif subject == "Geometry":
            avarage += score2[subject] * 2
            divider += 2
        else:
            avarage += score2[subject]
            divider += 1
    for subject in score3:
        if subject == "name":
            pass
        elif subject == "Algebra":
            avarage += score3[subject] * 2
            divider += 2
        elif subject == "Physics":
            avarage += score3[subject] * 2
            divider += 2
        elif subject == "Geometry":
            avarage += score3[subject] * 2
            divider += 2
        else:
            avarage += score3[subject]
            divider += 1
    for subject in score4:
        if subject == "name":
            pass
        elif subject == "Algebra":
            avarage += score4[subject] * 2
            divider += 2
        elif subject == "Physics":
            avarage += score4[subject] * 2
            divider += 2
        elif subject == "Geometry":
            avarage += score4[subject] * 2
            divider += 2
        else:
            avarage += score4[subject]
            divider += 1
    return avarage / divider


def sort_students(students):
    avarages = {}
    sorted_students = {}
    for student in students:
        avarages[student] = students[student]["Total Avarage"]
    avarages = {k: v for k, v in sorted(avarages.items(), key=lambda item: item[1], reverse=True)}
    for student in avarages:
        sorted_students[student] = students[student]
    return sorted_students


def write_to_ods(students, filename):
    from pyexcel_ods import save_data
    data = {"Sheet1": []}
    data["Sheet1"].append(["Name", "Academics", "IELTS", "Interview", "Total Avarage"])
    for student in students:
        temp = [student]
        for score in students[student].values():
            temp.append(score)
        data["Sheet1"].append(temp)
    save_data(filename, data)


if __name__ == "__main__":
    students = {}
    academics_term1 = ParseODS(input("[?] Path to 1st term of academics: "))
    academics_term2 = ParseODS(input("[?] Path to 2nd term of academics: "))
    academics_term3 = ParseODS(input("[?] Path to 3rd term of academics: "))
    academics_term4 = ParseODS(input("[?] Path to 4th term of academics: "))
    ielts = ParseODS(input("[?] Path to IELTS Results: "))
    interview = ParseODS(input("[?] Path to interview results: "))
    for student_name in academics_term1.get_students_names():
        students[student_name] = {}

    for student in students:
        students[student]["academics"] = get_avarage_of_all_academics(
            academics_term1.get_student(student),
            academics_term2.get_student(student),
            academics_term3.get_student(student),
            academics_term4.get_student(student)
        )
        students[student]["ielts"] = ielts.get_avarage(student)
        students[student]["interview"] = interview.get_avarage(student)

    for student in students.values():
        student["Total Avarage"] = 0.4*(student["academics"]/100)+0.3*(student["ielts"]/9)+0.3*(student["interview"]/10)
    
    students = sort_students(students)
    write_to_ods("output.ods", students)