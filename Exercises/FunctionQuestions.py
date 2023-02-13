print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
num = int(input("Please enter an integer: "))
def divisors(num:int) -> list:   # This function which takes in an inteher as an argument and returns the divisors of that number as a list
    result = []      # aasign an empty list
    for i in range(1, num+1):     #loops through each number from 1 to num
        if num % i ==0:      # checks for divisors of num
            result.append(i)  # append the divisors to the list
        return result     #Return the list of divisors to the list

print(f"The divisors of {num} are:", divisors(num))


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def test_number(num1, num2):
    if num1 % num2 ==0 or num2 % num1 ==0:
        return True
    else:
        return False
print(test_number(2, 6))    
#Prints - True

# --------------Example 2-------------------------- #


print("You must type two integers to find if one of the numbers is a factor of the other")
num1 = int(input("Enter the first integer: "))
num2 = int(input("Enter the second integer: "))
def integers(num1: int, num2: int) -> bool: #This function takes in two integers as arguments and returns true if one of the numbers is a factor of the other,false otherwise
     if num1 % num2 == 0 or num2 % num1 == 0: # division to find if one of the numbers is a factor of the other        
        return True
     else:
        return False
print(f"For the integers {num1} and {num2} being a factor of the other, the result is:", integers(num1, num2))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:

letter = str(input("Letter you want to know position of: "))
def alphabet_position(letter):
    for i in letter:
        answer = alphabet.index(i)
        return answer

print(alphabet_position(letter))

# --------------Example 2-------------------------- # 
#Both calculation gives the same output


user_input = str(input("Enter a letter to return its position in the alphabet: "))
def letter(l: str) -> int: #This function takes a letter (as a string) as an input and outputs it's position in the alphabet
    return alphabet.index(l)
print(f"Letter '{user_input}' position in the alphabet is:", letter(user_input))

print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

name = str(input("Type your name to produce an ID: "))

def id(name):
    position = '' 
    for i in name.lower():
        position += str(alphabet_position(i)) 
    return position

print('Your ID Number is: ', id(name))


print("\nQ2c\n")
# Q2c: Create a function which turns this yID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:

name = str(input("Enter your name to generate a password: "))
def person(name: str) -> str: #This function takes a persons name as an input string \n and returns an ID number consisting of the positions of each letter in the name
    position = ""
    for n in name.lower():
        position += str(alphabet.index(n)) # append all letters indexes
    return position

def id_password(position: int) -> str: #This function turns this ID into a password. \n The function should subtract the sum of the numbers in the id that was generated from the whole number of the id
    id_sum = sum(int(i) for i in position) # sum up all the id numbers index    
    password = int(position) - id_sum # subtract the sum of the id numbers generated from the position variable
    return str(password) # return password as a string
    
position = person(name)
print(f"Your password is:", id_password(position))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

user_input = int(input("Enter an integer: "))

def prime_num(num: int) -> bool:  #This function takes an integer as an input, and returns true if the number is prime, false otherwise

    if num < 2:
        return False # if statement to exclude integer 1
    for n in range(2, num): # loops through the range 2 to user input
        if num % n == 0:
            return False # returns false any number divisible by other number in specified range
        return True # if none of the above conditions are met, then the input number is prime

print(f"The integer {user_input} returns:", prime_num(user_input))



print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

user_input = input("Enter an integer: ")
def prime_num(num: int) -> bool: # This function takes an integer as an input, and returns true if the number is prime, false otherwise"""    
    try:
        num = int(num)
        if num < 2:
            return False # if statement to exclude integer 1
        for n in range(2, num): # loops through the range 2 to user input
            if num % n == 0:
                return False # returns false any number divisible by other number in specified range
            return True # if none of the above conditions are met, then the number is prime
    except (ValueError, NameError):
        return "Please enter a valid number." # displays the message for invalid user input

print(prime_num(user_input))

# -------------------------------------------------------------------------------------- #

