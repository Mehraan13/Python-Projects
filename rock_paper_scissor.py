import random

choices = ['Rock', 'Paper', 'Scissor']

user_in = input("rock(0)...paper(1)...scissor(2): ")

if user_in.isdigit(): user_in = int(user_in)

num = random.randint(0,2)
computer_choice = choices[num]

print("Computer: ", computer_choice, " You chose: ", choices[user_in])

if num == 0 and user_in == 0 or num == 1 and user_in == 1 or num == 2 and user_in == 2:
    print("both same :(")
    quit()

if num == 0 and user_in == 1:
    print("You win")
elif num == 0 and user_in == 2:
    print("you looose!")
elif num == 1 and user_in == 0:
    print("you loose!")
elif num == 1 and user_in == 2:
    print("You win")
elif num == 2 and user_in == 0:
    print("You win")
else:
    print("you loose")