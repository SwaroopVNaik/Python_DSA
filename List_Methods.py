# Python List Methods :->

# Python_Lists (Array) 👇 !
numbers = [1, 3, 2]

# Methods in Python_list 👇 !

# append - Function..! 
numbers.append(4) # appending Value 4 in number[] List..!
numbers.append(7) # appending Value 7 in number[] List..!
numbers.append(5) # appending Value 5 in number[] List..!

print("\nThe Appended Values of List -> numbers [1, 3, 2] is =>", numbers)

# Sort - Function..!

print("\nThe UnSorted List =>", numbers)
numbers.sort() # It will sort the values in the List in ascending Order ( increasing order)

print("\nThe Sorted List =>", numbers)

# Insert - Function..!

# Generic - Syntax => numbers.Insert(Index, value)
# Index => Declare the index value where you want to insert the Value in List
# Value => Declare The value which we want to insert In the declared Index of List 

number_2 = [2, 8, 0]

print("\nBefore Inserting the values in the List", number_2)

number_2.insert(0, 700)

print("\nAfter Inserting values in the List =>", number_2)

# remove - Function..!

print("\nBefore removing the values of List =>", number_2)

number_2.remove(700)

print("\nAfter removing the values of List =>", number_2)

# reverse - function..!

print("\nBefore reversing the Values in String => ", numbers)

numbers.reverse()

print("\nAfter Reversing the Value of the String => ", numbers)

# pop - function..!

# Generic - syntax => numbers.pop(Index)
# if we dont declare any index number in the pop it pops the last index values from List
# if we declare the pop index values of the List, it will pop the declared index value from List 

print("\nBefore Popping the values from the List => ", numbers)

numbers.pop(4)

print("\nAfter Poping the elements from the List => ", numbers)

# Accessing the Elements from the List 👇 !

for number in numbers:
    print(number)

# 2 - Dimensional List In python (2-D Array)
# 2 - row's , 3 - coloumn's 

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print("\nThe 2-Dimensional List => ", matrix)

# changing the values in 2-Dimensional Arrays

print("\nBefore Change The values Of 2-Dimensional List => ", matrix)

matrix[0][0] = 100 # changing value of 0th row index and coloumn value -> 100
matrix[0][1] = 200 # changing value of 0th row index and 1st coloumn Index Value -> 200

matrix[1][0] = 7 # changing value of 1st row index and 0th coloumn index value -> 7
matrix[1][1] = 888 # changing value of 1st row index and 1st coloumn index value -> 888

print("\nAfter Change The values Of 2-Dimensional List => ", matrix)


















