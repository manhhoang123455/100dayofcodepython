from tabnanny import check
from game_data import data
from art import logo,vs
import random

def get_random_account():
    return random.choice(data)

def format_account(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, {description}, from {country}"

def check_answer(guess,account_a,account_b):
    if account_a['follower_count'] > account_b['follower_count']:
        guess == 'a'
    else:
        guess == 'b'
    return guess
def game():
    print(logo)
    score = 0
    game_should_continue = True
    while game_should_continue:
        account_A = get_random_account()
        account_B = get_random_account()
        print(f"Compare A: {format_account(account_A)}")
        print(vs)
        print(f"Compare B: {format_account(account_B)}")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        is_correct = check_answer(guess,account_A,account_B)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_should_continue =False

game()