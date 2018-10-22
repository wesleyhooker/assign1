#!/usr/bin/env python3
"""
Validates that the user enteres the correct PIN number
"""

def valid_input(input):
    """
    Checks for valid PIN Number

    Argument:
        input = the users inputted PIN
    Returns:
        Any Errors with the input
        TRUE if it passes, False if it doenst
    """
    if(len(input) != 4):
        print("Invalid PIN length. Correct format is: <9876>")
        return False
    elif(not input.isdigit()):
        print("Invalid PIN character. Correct format is: <9876>")
        return False
    elif(input != "1234"):
        print("Your PIN is incorrect")
        return False
    elif(input == "1234"):
        print("Your PIN is correct")
        return True


def main():
    """
    Tests the valid_Input() function to make sure that the user entered pin
    is corrrect
    If user enters wrong pin 3x they are blocked from the account
    If they enter correct it is accepted

    Exit 0 if correct PIN
    Exit 1 if Incorrect PIN 3x
    """
    i = 0
    while (i !=3): #allow input for 3 tries
        userInput = input("Enter your PIN: ")
        if(valid_input(userInput)):
            exit(0)
        else:
            i = i + 1 #incriment i
    if (i == 3): #after 3 tries, block account.
        print("Your bank card is blocked")
        exit(1)


if __name__ == "__main__":
    main()
    exit(0)
