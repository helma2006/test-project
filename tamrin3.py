def calculate_student_gpa(grades):
    total = sum(grades)
    count = len(grades)
    gpa = total / count
    return gpa
 
students_list = [
    {
        "student_id": 1,
        "name": "ali",
        "grades": [18, 19, 20]
    },
    {
        "student_id": 2,
        "name": "amir",
        "grades": [15, 14, 16.5]
    },
    {
        "student_id": 3,
        "name": "reza",
        "grades": [17, 16, 18.5, 19]
    }
]

print("moadel daneshjoyan")
for student in students_list:
    gpa = calculate_student_gpa(student["grades"])
    print(f"{student['name']} (student_id : {student['student_id']}): moadel = {gpa:.2f}")