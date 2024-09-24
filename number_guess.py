import random

score = 0

game_on = True
number = random.randint(1,10)

while game_on:
    
    

    users_guess = int(input("Your guess (1,10) ?: "))

    if users_guess == number:
        print("Yay! you are right")
        score +=1
        print(f"Your score is: {score}")
        number = random.randint(1,10)
    else:
        place = 'above' if users_guess > number else 'below'
        print(f'You were {place} the number')

    i = input("wanna try again? (y/n)").lower()

    if i != 'y':
        game_on = False

