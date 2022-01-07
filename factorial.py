#!/usr/bin/env python3

# Created by: Ketia Gaelle Kaze
# Created on: Jan. 6, 2022
# This program asks the user to enter a whole number
# and then uses a loop to calculate and display the factorial
# of the user number from 1 to the number the user entered.

def main():
    # initialize the loop counter and factorial answer
    loop_counter = 0
    factorial_answer = 1

    # get the user number as string
    user_number_string = input("Enter a whole number: ")
    print("")

    # checks the errors
    try:
        # changes user number as string to an integer
        user_number = int(user_number_string)
        # checks to see if the user number is a whole number
        if (user_number >= 0):
            # calculate the factorial of the user number
            while True:
                loop_counter = loop_counter + 1
                factorial_answer = factorial_answer * loop_counter
                print("Tracking {} times through the loop."
                      .format(loop_counter))
                if loop_counter >= user_number:
                    break

            print("")
            print("{}! = {} ".format(user_number, factorial_answer))

        else:
            print("{} is not a whole number.".format(user_number_string))
    except Exception:
        print("{} is not a number.".format(user_number_string))
    finally:
        print("")
        print("Thanks for playing! ")


if __name__ == "__main__":
    main()
