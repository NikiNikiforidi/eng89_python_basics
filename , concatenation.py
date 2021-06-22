# Using and managing string
# String concatenation
# Casting methods
# Signle and double quotse
'''
single_quotes = 'These are single'
double_quotes = "These are double"

print(single_quotes)
print(double_quotes)
print( "Use double so you can use single quote in sentence, ex: Niki's house")

# Concatination
print(single_quotes + ' ' + double_quotes)
first_name = 'Niki'
middle_name = 'Maria'
last_name = 'Nikiforidi'

'''

'''
# Create a variable called age (int) and display age in the same line as name

first = input("Enter first name:")
last = input("Enter last name: ")
age =24 #int
print(first + ' ' + last + ' ' + str(age)) # can't merge different types
# str(age) casting the age from int to string 


age = int(input("Enter age:"))
print(type(age))
print(first + ' ' + last + ' ' + age) # can't merge different types
'''

# String slicing and indexing
'''
greatings = "Hello world" #index starts at 0

print(len(greatings)) #prints length

print(greatings[0:5])    # DOES NOT INCLUDE 5
print(greatings[6:12])   # slice string from index 6 to 11

print(greatings[-5:-1])    # slices string left to right, starting from -1
'''

'''
#   string built in methods

white_spaces = "Lots of what spaces           "
print(len(white_spaces)) # it also counts spaces

# strip() removes all the while spaces
print(len(white_spaces.strip()))

'''

# more built in methods to use with string

example_text =" here is some TEXT with let's of TEXT"

print(example_text.count("TEXT")) # to check for any repeats

print(example_text.lower()) # creates all lower case text
print(example_text.upper()) # creates all upper case text
print(example_text.title()) # changes first letter of each word to capital
print(example_text.capitalize()) # changes first letter of sentence to caps
print(example_text.replace("some", " 'a bit off' "))







