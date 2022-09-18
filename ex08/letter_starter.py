#!/usr/bin/env python3
import sys


def read_and_write(input_email):
    with open('employees.tsv', 'r') as input_file:
        for line in input_file:
            name, surname, email = line.strip("\n").split("\t")
            if email == input_email:
                print(f"Dear {name}, welcome to our team. We are sure that it will be a pleasure to work with"
                      "you. That’s a precondition for the professionals that our company hires.")
                return


if __name__ == '__main__':
    if len(sys.argv) == 2:
        read_and_write(sys.argv[1])
