import rpsfunc

comp_score = 0
user_score = 0

while comp_score < 3 and user_score < 3:

    # Call on my function here
    user_choice = rpsfunc.convert_user_choice()

    # Call on my function here
    comp_choice = rpsfunc.convert_comp_choice()

    # Call on my game function here
    outcome = rpsfunc.game(user_choice, comp_choice)

    print(outcome, 'You chose', user_choice, 'and the computer chose', comp_choice,)

    user_score = rpsfunc.scoring_user(outcome)
    print('User score is', user_score)
    comp_score = rpsfunc.scoring_comp(outcome)
    print('Computer score is', comp_score)

else:
    print('User score is', user_score, 'Computer score is', comp_score, 'The game has now ended.')