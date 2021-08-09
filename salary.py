#!/usr/bin/python3

def staff(name):
    #    name = 'Jay'
    salary = 1500
    #    bonus = 0
    # Loops
    if name == 'Juan':
        bonus = 300
    elif name == 'Jay':
        bonus = 400
    elif name == 'Blue':
        bonus = 500
    else:
        bonus = salary * 0.1
    print(bonus)


staff('Blue')
