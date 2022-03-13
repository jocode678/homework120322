import math


def input_values():
    value_list = []
    value_input = print('When you are finished entering numbers, press enter')
    while value_input != '':
        value_input = input('Enter a number: ')
        if value_input == '':
            break
        value_list.append(float(value_input))
    return value_list


def operation():
    operator_input = input('Enter an operator (+, -, * or /): ')
    if operator_input == '+':
        print('The sum of all values inputted equals', sum(user_values))
    elif operator_input == '-':
        print('All values taken away from each other equal', subtractList(user_values))
    elif operator_input == '*':
        print('The sum of all values multiplied together equal ', math.prod(user_values))
    elif operator_input == '/':
        print('All values divided by each other equal', divideList(user_values))


def subtractList(user_values):
    result = user_values[0]
    for value in user_values[1:]:
        result -= value
    return result


def divideList(user_values):
    try:
        result = user_values[0]
        for value in user_values[1:]:
            result /= value
        return result
    except ZeroDivisionError:
        print('You cannot divide by zero')


answer = input('Would you like to do a calculation? Type yes or no: ')
while answer != 'yes' and answer != 'no':
    print('Answer the question properly')
    answer = input('Would you like to do a calculation? Type yes or no: ')
else:
    while answer == 'yes':
        user_values = input_values()
        print(user_values)
        operation()
        answer = input('Would you like to do another calculation? Type yes or no: ')
    else:
        print('You do not have to play with the calculator anymore.')