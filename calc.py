import calc_funcs

user_values = []

answer = input('Would you like to do a calculation? Type yes or no: ')
while answer != 'yes' and answer != 'no':
    print('Answer the question properly')
    answer = input('Would you like to do a calculation? Type yes or no: ')
else:
    while answer == 'yes':
        user_values = calc_funcs.input_values()
        print(user_values)
        calc_funcs.operation()
        answer = input('Would you like to do another calculation? Type yes or no: ')
    else:
        print('You do not have to play with the calculator anymore.')