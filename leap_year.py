#!/usr/bin/env python3
# Created By: Emmanuella Taiwo
# created on 28th Oct, 2026
# This program asks the user for a year number as a string
# and casts it into an integer and
# displays if the year is a leap year or not


def main():
    # this function checks if the year is a leap year or not
    # input
    year_as_string = input("Enter a year: ")
    print("{year}".format(year=year_as_string))

    # process & output
    try:
        year_as_integer = int(year_as_string)
        if (year_as_integer % 4 == 0 and year_as_integer % 100 != 0) or (
            year_as_integer % 400 == 0
        ):
            print("{year} is a leap year".format(year=year_as_integer))
        else:
            print("{year} is not a leap year".format(year=year_as_integer))
    except Exception:
        print(
            "{year} is an invalid input,enter a valid integer".format(
                year=year_as_string
            )
        )


if __name__ == "__main__":
    main()
