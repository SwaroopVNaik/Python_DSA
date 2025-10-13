# Time complexity : O(n)
def find_student(name):
    for student in enrolled_student_names:
        if student == name:
            print(f"{name} is found in the list")
            return
    print(f"{name} is not found in the list")
#----------------------------------------------------------------------------------------
def find_student_usingset(): 
    if ("Amit" in enrolled_student_names): # Time complexity to search is O(1)
        print("Amit is found in the list")
    else:
        print("Amit is not found in the list")

    print("Amit" in enrolled_student_names)
#---------------------------------------------------------------------------------------
def student_data_analysis():

    # Students who have enrolled in the course and also paid the fees 
    # They must be present in both the list - enrolled and paid 
    paid_enrolled = enrolled_student_names & paid_course_student_names
    print("List of enrolled and paid students are ")
    print(paid_enrolled)

    all_the_students = enrolled_student_names | paid_course_student_names
    print("List of all the students")
    print(all_the_students)

    unpaid_students = enrolled_student_names - paid_course_student_names
    print("List of students who need to pay the fees")
    print(unpaid_students)

    yet_to_enroll_but_paid_fees = paid_course_student_names - enrolled_student_names
    print("Students who paid fees but not yet enrolled ")
    print(yet_to_enroll_but_paid_fees)

    call_from_customercare_final_list = paid_course_student_names ^ enrolled_student_names
    print("Need to be followed-up by our customer care team")
    print(call_from_customercare_final_list)
#-------------------------------------------------------------------------------------------
if __name__ == "__main__":

    enrolled_student_ids = { 100, 200, 101, 205, 305}

    print(enrolled_student_ids)

    enrolled_student_names = { "Mahesh", "Mahesh", "Mahesh", "Santosh", "Sushil", "Amit", "Mahesh Bisur", "Sangeeta"}

    print(enrolled_student_names)

    find_student("Amit")
    find_student_usingset()


    paid_course_student_names = { "Santosh", "Sushil", "Vidya"}

    student_data_analysis()   