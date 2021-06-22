# Python Basics

- Test installation and pycharm
```
print("hello world")
```

#### Variables: They work as a placeholder to store data
- Strings: "anything between quotes"
- Integers: numbers
- Syntax to create a variable name of the variable = vale of variable
```
First_Name = "Niki"
Last_Name = "Nikiforidi"

Salary = 10.5 # float value
Age = 24 # int value
my_age = 22
```
```
print(First_Name)
print(Last_Name)
print(Salary)
print (Age)
print(my_age)
```

- type() find the type of variable

```
print(type(Age)) # Integer
print(type(Salary)) # Float
print(type(First_Name)) # String
```

- print(First_Name+1) # Error message: can only concatenate str (not "int") to str

- To interact with user: input()
```
User_Name=input("Please unter your name: " )
print("Hello :)")
print(User_Name)
```

**TASK:Create variables: first_name, last_name, age, DoB**
- Prompt user to input above values
- Print/display the type of each value received from the user
- Then display the data back to user with generating message

```
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

```



#### Using and managing string
- String concatenation
- Casting methods
- Single and double quotes

```
single_quotes = 'These are single'
double_quotes = "These are double"

print(single_quotes)
print(double_quotes)
print( "Use double so you can use single quote in sentence, ex: Niki's house")
```


- Concatination
```
print(single_quotes + ' ' + double_quotes)
first_name = 'Niki'
middle_name = 'Maria'
last_name = 'Nikiforidi'
```


# Create a variable called age (int) and display age in the same line as name
```
first = input("Enter first name:")
last = input("Enter last name: ")
age =24 #int
print(first + ' ' + last + ' ' + str(age)) # can't merge different types
# str(age) casting the age from int to string 


age = int(input("Enter age:"))
print(type(age))
print(first + ' ' + last + ' ' + age) # can't merge different types
```

- String slicing and indexing

```
greatings = "Hello world" #index starts at 0

print(len(greatings)) #prints length

print(greatings[0:5])    # DOES NOT INCLUDE 5
print(greatings[6:12])   # slice string from index 6 to 11

print(greatings[-5:-1])    # slices string left to right, starting from -1
```


- String built in methods

```
white_spaces = "Lots of what spaces           "
print(len(white_spaces)) # it also counts spaces
```

- strip() removes all the while spaces
```
print(len(white_spaces.strip()))
```


- More built in methods to use with string

```
example_text =" here is some TEXT with lots of TEXT"

print(example_text.count("TEXT")) # to check for any repeats

print(example_text.lower()) # creates all lower case text
print(example_text.upper()) # creates all upper case text
print(example_text.title()) # changes first letter of each word to capital
print(example_text.capitalize()) # changes first letter of sentence to caps
print(example_text.replace("some", " 'a bit off' "))
```






#### What are data types and operators
- Data types: boolean, numbers and strings
- Arithmetic operators + - * / % (modulus)
- Comparison operators : > < == != >= <=


- Mathematics operators
```
number_1 = 4
number_2 = 2

print(number_1 + number_2)
print(number_1 - number_2)
print(number_1 * number_2)
print (number_1 / number_2)     # when you divide numbers it returns float
print (number_1 % number_2)
print (number_1 ** number_2)    # exponential
```

- Boolean
```
print(number_1 == number_2)     # Is num1 equal to num2?
print( number_1 != number_2)
print( number_1 >= number_2)
print(number_1 <= number_2)
```





