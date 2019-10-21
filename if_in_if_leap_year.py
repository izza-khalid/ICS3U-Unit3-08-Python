#!/usr/bin/env python3

# Created by: Izza Khalid
# Created on: October 2019
# This program uses a nested if statement
# with user input


def main():
    # this function uses a nested if statement

    # input
    leap_year = int(input("Enter a year from the past, present or future: "))
    print("")

    # process & output
    if (leap_year % 4) == 0:
        if (leap_year % 100) == 0:
            if (leap_year % 400) == 0:
                print("It's a leap year!")
            else:
                print("It’s not a leap year.")
        else:
            print("It’s a leap year.")
    else:
        print("It’s not a leap year.")


if __name__ == "__main__":
    main()
