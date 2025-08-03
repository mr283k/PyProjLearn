# programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected."
#     , "Function": "A piece of code that you can easily call over and over again."}
#
# for key in programming_dictionary:
#     print(key)

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}


# def convert_grades(student_scores, student_grades):
#     for names in student_scores:
#         if student_scores[names] > 90:
#             student_grades[names] = "Outstanding"
#         elif 81 <= student_scores[names] <= 90:
#             student_grades[names] = "Exceeds"
#         elif 71 <= student_scores[names] <= 80:
#             student_grades[names] = "Acceptable"
#         elif student_scores[names] <= 70:
#             student_grades[names] = "Fail"
#         else:
#             print("out of range")
#         student_grades += student_grades
#     print(student_grades)

def convert_grades(student_scores, student_grades):
    for names in student_scores:
        if student_scores[names] > 90:
            student_grades[names] = "Outstanding"
        elif 81 <= student_scores[names] <= 90:
            student_grades[names] = "Exceeds"
        elif 71 <= student_scores[names] <= 80:
            student_grades[names] = "Acceptable"
        elif student_scores[names] <= 70:
            student_grades[names] = "Fail"
        else:
            student_grades[names] = "out of range"
    print(student_grades)

student_grades = {}
convert_grades(student_scores, student_grades)
