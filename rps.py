import rpsfunc


answer = input('Would you like to play rock paper scissors? (yes/no) ')
while answer == 'yes':

    # Call on my function here
    user_choice = rpsfunc.convert_user_choice()

    # Call on my function here
    comp_choice = rpsfunc.convert_comp_choice()

    # Call on my game function here
    outcome = rpsfunc.game(user_choice, comp_choice)

    print(outcome, 'You chose', user_choice, 'and the computer chose', comp_choice,)
    answer = input('Would you like to play again? ')

else:
    print('The game has now ended.')