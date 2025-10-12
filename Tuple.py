""" 
Characteristics of Tuple ->
-> Immutable ( Cannot change the value once declared)
-> Ordered (It stores the Elements in an order)
-> Allows Duplicate (We Can Declare same Multiple Elements)

The Tuple is Stored in Heap Memory !
The Tuples are More efficient then Lists !
Time Complexity of Tuple when Asscessing elements is O(1)

"""
#------------------------------------------------------------------------------------------------------------------
# Syntax Of Tuple ->
# Observe Tuples use Circular Brackets while List Square Brackets
# Tuples can be declared In two ways/methods ->
# Method_1 of Declaring Tuples 👇 :-> 
# packing -> Assigning all the values of tuple to one variable and printing them 
student_1 = ("Mahesh Arali Sir", "SDE Full stack ", "20 years Industry Experiance", 42) # -> Packing 

print(student_1)
#------------------------------------------------------------------------------------------------------------------
# To print The Each Element Using Index Value ->
print(student_1[0])
print(student_1[1])
print(student_1[2])
print(student_1[3])

""" -> student[3] = 40 ( we cannot Add(overide) new elements in Tuple once its Declared, 
Either once we use the declared tuple or 
we hv to throw it and Create a new tuple but cannot add new element to the Exsiting Tuple) """
#------------------------------------------------------------------------------------------------------------------
# Method_2 of Declaring Tuples 👇 :-> 
# packing -> Assigning all the values of tuple to one variable and printing them 
student_2 = "Swaroop", "Aspiring SDE Full stack ", "Learning with algorithms365", 21 # -> Packing

print(student_2)
#-----------------------------------------------------------------------------------------------------------------
# To print The Each Element Using Index Value ->
print(student_2[0])
print(student_2[1]) 
print(student_2[2])
print(student_2[3])
#----------------------------------------------------------------------------------------------------------------
# Tuples May be Nested ->

country = "Bharat", student_2

print(country)
#-----------------------------------------------------------------------------------------------------------------
# declaring Tuple with Single data
Tuple_Single_Data = "India",
print(Tuple_Single_Data)
#-----------------------------------------------------------------------------------------------------------------
# Reverse Operation Of Tuple
student_3 = "SVN", "CSE", "4th year", 21
# Assinging the value of tuple (student_3) to each new Variable and printing them , this un-packing 
name, dept, year, age = student_3 # -> Un-Packing

print(name)
print(dept)
print(year)
print(age)
#------------------------------------------------------------------------------------------------------------------
# Usage of Tuple :->
# Returning Multiple Values from the Function
# Function_Declaration 👇 :->
def return_student_marks(name):
    # Dummy Code or Logic
    return 90, 99, 100, 75 
"""In python it takes these values and creates a tuple,
Makes this Tuple a object and store in RAM(HEAP MEMORY)
and Return the Reference of the Object"""
# We might feel its returning Multiple Values, when writing the code 😂 !!!
""" -> we cannot return mutiple Values from function Like this directly in C , C#, java 
    and so many other Programming Languages """
# Function_Invokation 👇 :->
student_marks = return_student_marks("Swaroop")
print(student_marks)
#-----------------------------------------------------------------------------------------------------------------
# Operations in Tuple 

# Returns Number of elements in Tuple
# student_1.count() -> Takes Only One Argument
#------------------------------------------------------------------------------------------------------------------
# Craeting a Tuple 
Colleges = "SVIT", "RVCE", "PES", "RV", "SVIT", "KLE", "SVIT"
# This Operations (Occurance Count) is very useful when dealing with thousands of Data
# we need count of one particular data example -> college, person etcetc we can use the operations
count = Colleges.count("SVIT")
print(f"The Number of Students from SVIT = {count}")

#-----------------------------------------------Thank-You------------------------------------------------------------