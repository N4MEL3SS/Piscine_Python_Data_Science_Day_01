#!/usr/bin/env python3
import sys


def read_and_write(filename):
    with open(filename, 'r') as input_file:
        with open('employees.tsv', 'w') as output_file:
            output_file.write("Name\tSurname\tE-mail\n")
            for line in input_file:
                name_surname = line.split("@")
                name, surname = name_surname[0].split(".")
                output_file.write(f"{name.capitalize()}\t{surname.capitalize()}\t{line}")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        read_and_write(sys.argv[1])
