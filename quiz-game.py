print("Welcome to Shivang's Computer Quiz!")

playing = input("Would You like to play this Informative Game? ").lower()

if playing != 'yes':
    quit()

print("Welcome to my Quiz Game! let's play:)")


name = input("To start off : what is your name? ")
print(f"welcome {name}, make sure to check out the github repository for more quizzes")

score = 0

Question_1 = input("What does CPU stand for? ")
if Question_1.lower() == "central processing unit":
    print("correct ")
    score += 1
else:
    print("incorrect ")

Question_2 = input("What does RAM stand for? ")
if Question_2.lower() == "random access memory":
    print("correct ")
    score += 1
else:
    print("incorrect ")

Question_3 = input("What does GB stand for? ")
if Question_3.lower() == "gigabyte":
    print("correct ")
    score += 1
else:
    print("incorrect ")

Question_4 = input("What does GPU stand for? ")
if Question_4.lower() == "graphics processing unit":
    print("correct ")
    score += 1
else:
    print("incorrect ")

print("you got " + str(score) + " questions correct!")
print("you got " + str((score/4)*100) + "%.")
