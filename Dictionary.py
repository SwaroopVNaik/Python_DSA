# Creating a Dictionary < (KEY) | (VALUE) >
""" Note -> Both Set and Disctionary uses Curly Braces !
-> Dictionary uses curly braces with Key Value pair
-> Set Uses curly braces with only Values, Without Keys """
student_List_empty = {}

# To add Values In Dictionary
# Syntax : Variable_name_dictionary[key] = Value
student_List_empty[1] = "ZOHO"

car_list = {
    '001': "Toyota Fortuner",
    '002': "Mahindra 700",
    '003': "Tata Safari",
    '004': "Toyota Land Cruiser",
    '005': "Honda CR-V",
    '006': "Ford Explorer"
}

print(student_List_empty)

print(car_list)

# Searching the Elements And Printing
# This function (get) is able to retrive the data for O(1)
name = car_list.get('002')
print(f"Name Of the CAR : {name}")

#Removing the Data 
#Cars = car_list.pop("010") # <- when we are removing a key which is not present in Dictionary we get a (KEY ERROR : '010')

#print(f"The car Name is : {Cars}")

Cars_1 = car_list.pop('005')
print(f"Removed Value is : {Cars_1}")

# Extarcting only Keys : 
print(car_list.keys())

# Extracting Only Values :
print(car_list.values())

# Deleting all the Entries In the Dictionary :
car_list.clear()

print(car_list)


"""The student_directory dictionary holds student IDs as keys, 
with each value being another dictionary that contains the student's name and branch of study."""
student_directory = {
    101: {"name": "Alice", "branch": "Computer Science"},
    102: {"name": "Bob", "branch": "Electronics"},
    103: {"name": "Charlie", "branch": "Mechanical"},
    104: {"name": "David", "branch": "Civil Engineering"},
    105: {"name": "Eva", "branch": "Electrical Engineering"},
    106: {"name": "Frank", "branch": "Chemical Engineering"}
}

student_1 = student_directory[101]
print(f"The Value Asscessed is : {student_1}")

student_1 = student_directory[105]
print(f"The Value Asscessed is : {student_1}")

# Updating 
student_1 = student_directory[101]["name"] = "Swaroop"
print(f"The updated Dictionary : {student_1}")

print(student_directory.get(101)) # -> Time Complexity O(1)