import random, time

#declare constants
OPERATORS = ['+','-','//','*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND,MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + ' ' +  operator + ' ' + str(right)
    answer = eval(expr) #evaluates an expression in string format

    return expr, answer


wrong = 0
input("Press Enter to start!")
print('-'*10)

#timer
start_time = time.time()

#main body
for i in range(TOTAL_PROBLEMS):
    expr, answer = generate_problem()
    while True:
        user_in = input("Problem #" + str(i+1) + ': ' + expr + ' = ')
        if user_in == str(answer):
            break
        else:
            print("Wrong Answer")
            wrong += 1

print('Your total time was: ' ,round(time.time() - start_time,2) , ' seconds')
print("You got ", wrong, ' wrong!')