#!/usr/bin/env python3
import sys


clients = [
    'andrew@gmail.com',
    'jessica@gmail.com',
    'ted@mosby.com',
    'john@snow.is',
    'bill_gates@live.com',
    'mark@facebook.com',
    'elon@paypal.com',
    'jessica@gmail.com']

participants = [
    'walter@heisenberg.com',
    'vasily@mail.ru',
    'pinkman@yo.org',
    'jessica@gmail.com',
    'elon@paypal.com',
    'pinkman@yo.org',
    'mr@robot.gov',
    'eleven@yahoo.com']

recipients = [
    'andrew@gmail.com',
    'jessica@gmail.com',
    'john@snow.is']


def call_center():
    # return list(set(clients) - set(recipients))
    return list((set(clients) | set(participants)) - set(recipients))


def potential_clients():
    return list(set(participants) - set(clients))


def loyalty_program():
    return list(set(clients) - set(participants))


def select_task(text):
    if text == "call_center":
        return call_center()
    elif text == "potential_clients":
        return potential_clients()
    elif text == "loyalty_program":
        return loyalty_program()
    else:
        raise Exception("Unknown task!")


if __name__ == '__main__':
    if len(sys.argv) == 2:
        print(select_task(sys.argv[1]))
