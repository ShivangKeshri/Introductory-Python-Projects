import random

maximum_range = input("Type a number: ")

if maximum_range.isdigit(): # returns true if the statement above is a digit
    maximum_range = int(maximum_range)

    if maximum_range <= 0:
        print('type a number larger than 0 next time')
        quit()
else:
    print('please type a number next time.')
    quit()

random_number = random.randint(0, maximum_range)
guesses = 0
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('please type a number next time.')
        continue

    if user_guess == random_number :
        print('you got it!')
        break
    elif user_guess > random_number: 
        print('you were above the number!')
    else:
        print('you were below the number!')

print(f"you got it in {guesses}", "guesses")
