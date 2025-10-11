# Creating a Database
students_db = []

def add_Student():
    # Typecasting to convert string to Integer
    id = int(input("Enter the Student_ID :"))
    name = input("Enter the Student_Name: ")

    # Tuple
    student_record = (id, name)
    # appending :-> adding at last Index of tuple (students_db)
    students_db.append(student_record)

def Print_all_Students():
    for student_record in students_db:
        print(student_record)



if __name__ == "__main__":
    add_Student()
    add_Student()
    add_Student()

    Print_all_Students()

#-------------------------------Thank-You-------------------------------