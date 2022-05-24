import random
import string
import time

def Generate_password():
     password = []
     for _ in range(int(lowercase_letters_number)):
          password.append(random.choice(string.ascii_lowercase))
     for _ in range(int(uppercase_letters_number)):
          password.append(random.choice(string.ascii_uppercase))
     for _ in range(int(digit_number)):
          password.append(random.choice(string.digits))
     for _ in range(int(special_characters_number)):
          password.append(random.choice(string.punctuation))
     random.shuffle(password)
     return password
def Info_about_number_not_in_range(number):
     if(number.isdecimal() == False):
          print("Looks like you did not enter a positive integer. Try again")
     elif (int(number) < 1):
          print("You need to have at least one character for each type. Try again")
     elif(int(number) > characters_left):
          print("That's more than you have. Try again")
     elif(characters_left - int(number) < types_left):
          print("In that case you would not have enough letters for the remaining character types. Try again")

def Loop_to_get_the_right_input(number, type):
     global characters_left
     global types_left
     types_left -= 1
     while (number.isdecimal() == False or int(
             number) > characters_left or characters_left - int(
             number) < types_left or int(number) < 1):
          Info_about_number_not_in_range(number)
          number = input("characters left:" + str(characters_left) + "\nEnter the number of " + type + " in the password")
     characters_left -= int(number)
     return number
types_left = 4
password_length = input("Enter the length of the password:")
while(password_length.isdecimal() == False or int(password_length) < 5 ):
     if(password_length.isdecimal() == False):
          print("Looks like you did not enter an integer. Try again")
     else:
          print("The password should not be shorter than 5 characters. Try again")
     password_length = input("Enter the length of the password:")
characters_left = int(password_length)

lowercase_letters_number = input("characters left:" + str(characters_left) + "\nEnter the number of lowercase letters in the password")
lowercase_letters_number = Loop_to_get_the_right_input(lowercase_letters_number, "lowercase letters")

uppercase_letters_number = input("characters left:" + str(characters_left) + "\nEnter the number of uppercase letters in the password")
uppercase_letters_number = Loop_to_get_the_right_input(uppercase_letters_number, "uppercase letters")

digit_number = input("characters left:" + str(characters_left) + "\nEnter the number of digits in the password")
digit_number = Loop_to_get_the_right_input(digit_number, "digits")

special_characters_number = input("characters left:" + str(characters_left) + "\nEnter the number of special characters in the password")
special_characters_number = Loop_to_get_the_right_input(special_characters_number, "special characters")

if(characters_left>0):
     lowercase_letters_number = str(int(lowercase_letters_number) + characters_left)
     print("The " + str(characters_left) + " left characters have been assigned to lowercase letters")
     characters_left = 0

time.sleep(1.5)
print("Final review:")
print("lowercase letters: " + lowercase_letters_number)
print("uppercase letters: " + uppercase_letters_number)
print("digits: " + digit_number)
print("special characters: " + special_characters_number)
time.sleep(3)
print("__THE PASSWORD__")
password = Generate_password()
print("".join(password))