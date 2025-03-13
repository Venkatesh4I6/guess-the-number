import random
EASY_LEVEL_ATTEMPTS=10
HARD_LEVEL_ATTEMPTS=5
def set_difficulty(level_chosen):
    if level_chosen=='easy':
        return EASY_LEVEL_ATTEMPTS
    elif level_chosen=='hard':
        return HARD_LEVEL_ATTEMPTS
    else:
        return
def check_answer(guessed_number,attempts,answer):
    if guessed_number<answer:
        print("your guess is too low")
        return attempts-1
    elif guessed_number>answer:
        print("your guess is too high")
        return attempts-1
    else:
        print("your guess is right... the answer was {answer}")
def game():
    print("let me think of a number between 1 to 50")
    answer=random.randint(1,50)
    print(answer)
    level=input("choose level of difficulty...type 'hard' or 'easy':")
    attempts=set_difficulty(level)
    if attempts!=EASY_LEVEL_ATTEMPTS and attempts!=HARD_LEVEL_ATTEMPTS:
        print("you have entered wrong difficulty level.. play again")
        return
    guessed_number=0
    while guessed_number!=answer:
        print(f"you have {attempts} attempts to guess the answer:")
        guessed_number=int(input("Enter any number"))
        attempts=check_answer(guessed_number,attempts,answer)
        if attempts==0:
            print("you are out of guesses...you lose:")
            return
        elif guessed_number!=answer:
            print("guess again")
game()
