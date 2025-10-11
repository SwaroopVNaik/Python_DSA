""" 
Characteristics of Tuple ->
-> Immutable ( Cannot change the value once declared)
-> Ordered (It stores the Elements in an order)
-> Allows Duplicate (We Can Declare same Multiple Elements)

The Tuple is Stored in Heap Memory !
The Tuples are More efficient then Lists !

"""
# Syntax Of Tuple ->
# Observe Tuples use Circular Brackets while List Square Brackets
# Tuples can be declared In two ways/methods ->
# Method_1 of Declaring Tuples 👇 :-> 
# packing -> Assigning all the values of tuple to one variable and printing them 
student_1 = ("Mahesh Arali Sir", "SDE Full stack ", "20 years Industry Experiance", 42) # -> Packing 

print(student_1)

# To print The Each Element Using Index Value ->
print(student_1[0])
print(student_1[1])
print(student_1[2])
print(student_1[3])

# -> student[3] = 40 ( we cannot Add(overide) new elements in Tuple once its Declared , Either once we use the declared tuple or we hv to throw it and Create a new tuple but cannot add new element to the Exsiting Tuple)

# Method_2 of Declaring Tuples 👇 :-> 
# packing -> Assigning all the values of tuple to one variable and printing them 
student_2 = "Swaroop", "Aspiring SDE Full stack ", "Learning with algorithms365", 21 # -> Packing

print(student_2)

# To print The Each Element Using Index Value ->
print(student_2[0])
print(student_2[1])
print(student_2[2])
print(student_2[3])

# Tuples May be Nested ->

country = "Bharat", student_2

print(country)

# declaring Tuple with Single data
Tuple_Single_Data = "India",
print(Tuple_Single_Data)

# Reverse Operation Of Tuple
student_3 = "SVN", "CSE", "4th year", 21
# Assinging the value of tuple (student_3) to each new Variable and printing them , this un-packing 
name, dept, year, age = student_3 # -> Un-Packing

print(name)
print(dept)
print(year)
print(age)