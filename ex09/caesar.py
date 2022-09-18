#!/usr/bin/env python3
import sys


def caesar(mode, plaintext, shift):
    ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    for char in plaintext:
        if ord(char) > 126:
            raise Exception("The script does not support your language yet.")
        elif char.isalpha() and char.islower():
            char = ascii_lowercase[(ascii_lowercase.find(char) + mode * shift) % 26]
        elif char.isalpha() and char.isupper():
            char = ascii_lowercase[(ascii_lowercase.find(char.lower()) + mode * shift) % 26].upper()
        res += char
    return res


if __name__ == '__main__':
    if len(sys.argv) == 4:
        if sys.argv[1].lower() == 'decode':
            print(caesar(-1, sys.argv[2], int(sys.argv[3])))
        elif sys.argv[1].lower() == 'encode':
            print(caesar(1, sys.argv[2], int(sys.argv[3])))
