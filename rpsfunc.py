# put functions outside of loop
# function for user choice

global_comp_score = 0
global_user_score = 0


def convert_user_choice():
    user_choice = input("Enter R, P or S for rock, paper or scissors: ")
    while user_choice not in ('R', 'P', 'S'):
        user_choice = input("You made an invalid choice. Please enter R, P or S for rock, paper or scissors: ")
    if user_choice == 'R':
        user_choice = 'rock'
    elif user_choice == 'P':
        user_choice = 'paper'
    elif user_choice == 'S':
        user_choice = 'scissors'
    return user_choice

# put imports outside of loop
import random

# function for comp choice
def convert_comp_choice():
    comp_choice = random.randint(0, 2)
    if comp_choice == 0:
        comp_choice = 'rock'
    elif comp_choice == 1:
        comp_choice = 'paper'
    elif comp_choice == 2:
        comp_choice = 'scissors'
    return comp_choice

# function to determine winner
def game(user_choice, comp_choice):
    if user_choice == comp_choice:
        outcome = 'You have drawn!'
    elif (user_choice == 'rock' and comp_choice == 'scissors') or (
            user_choice == 'paper' and comp_choice == 'rock') or (user_choice == 'scissors' and comp_choice == 'paper'):
        outcome = 'You have won!'
    elif (user_choice == 'rock' and comp_choice == 'paper') or (
            user_choice == 'paper' and comp_choice == 'scissors') or (
            user_choice == 'scissors' and comp_choice == 'rock'):
        outcome = 'You have lost :(.'
    return outcome



def scoring_comp(outcome):
    if outcome == 'You have lost :(.':
        global global_comp_score
        global_comp_score += 1
    return global_comp_score


def scoring_user(outcome):
    if outcome == 'You have won!':
        global global_user_score
        global_user_score += 1
    return global_user_score


