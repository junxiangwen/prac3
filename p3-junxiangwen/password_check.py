"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

from turtle import Turtle


MIN_LENGTH = 2
MAX_LENGTH = 6
SPECIAL_CHARS_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    while True:
        password=input("Enter your password:")
        if len(password) > 6:
            print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
        elif len(password)<2:
            print("Your password must be between", MIN_LENGTH, "and", MAX_LENGTH,
          "characters, and contain:")
        elif re.search("[0-9]",password) is None:
            print("\t1 or more numbers")
        elif re.search("[a-z]",password) is None:
            print("\t1 or more lowercase characters")
        elif re.search("[A-Z]",password) is None:
            print("\t1 or more uppercase characters")
        elif re.search("[!@#$%^&*()_-=+`~,./'[]<>?{}|\\]",password) is None:
            print("Invalid password!")
        else:
         print("Your {}-character password is valid: {}".format(len(password),password))


main()

        
            


            
