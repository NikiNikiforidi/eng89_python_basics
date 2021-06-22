'''
# testing installation
# right click to run

#print("hello world")

# print function os used to display outcome
# variables
# they work as a place holder to store data
# Strings: "anything between quotes"
# Integers: numbers
# Syntax to create a variable name of the variable = vale of veraible
First_Name = "Niki"
Last_Name = "Nikiforidi"
#
Salary = 10.5 # float value
Age = 24 # int value
my_age = 22

print(First_Name)
print(Last_Name)
print(Salary)
print (Age)
print(my_age)

# type() find the type of variable

print(type(Age)) # Integer
print(type(Salary)) # Float
print(type(First_Name)) # String

#print(First_Name+1) # Error message: can only concatenate str (not "int") to str

# To interact with user: input()
User_Name=input("Please unter your name: " )
print("Hello :)")
print(User_Name)
'''

# Askisi

# variables first_name, last_name, age, DoB
# Prompt user to input above values
# print/ display the type of each value received from the user
# then display the data back to user with generating message

first_name = input("Enter first name: ")
print(type(first_name))
print(first_name)

last_name = input("Enter last name: ")
print(type(last_name))
print(last_name)

age = input("Enter your age: ")
print(type(age))
print(age)

date_of_birth = input("Enter your date of birth: ")
print(type(date_of_birth))
print(date_of_birth)