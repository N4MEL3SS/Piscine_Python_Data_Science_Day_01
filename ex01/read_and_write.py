#!/usr/bin/env python3

def read_and_write(filename):
    with open(filename, 'r') as input_file:
        with open('ds.tsv', 'w') as output_file:
            new_text = input_file.read().replace('\",', '\"\t')
            new_text = new_text.replace('false,', 'false\t')
            new_text = new_text.replace('true,', 'true\t')
            output_file.write(new_text)


if __name__ == '__main__':
    read_and_write(input("Введите путь к файлу: "))
