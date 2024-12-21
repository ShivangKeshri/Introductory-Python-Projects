# generate a bunch of random math questions
# time them
# not be able to move forward without getting the answer correct.

import random
import time

operators = ["+","-","/","*"]
min_operand = 3
max_operand = 12
total_problems = 10

def generate_problem():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)

    expr = str(left) + "" + operator + " " + str(right)
    answer = eval(expr)
    print(expr)
    return expr, answer

wrong = 0
input("press enter to start!")
print("----------------------")

start_time = time.time()

for i in range(total_problems):
    expr, answer = generate_problem()
    while True:
        guess = input("Problem #" + str(i + 1) + ":" + expr + "=")
        if guess == str(answer):
            break
        wrong +=1
end_time = time.time()
total_time = end_time - start_time

print("----------")
print("congratulations!, You finished in ",total_time, "seconds!")
