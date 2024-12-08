print("Welcome to Shivang's Computer Quiz!")

playing = input("Would You like to play this Informative Game? ")

if playing != 'yes':
    quit()

print("Welcome to my Quiz Game! let's play:)")

name = input("To start off : what is your name? ")
print(f"welcome {name}, make sure to check out the github repository for more quizzes")

Question_1 = input("What does CPU stand for? ")
if Question_1 == "Central Processing Unit":
    print("good job! you can advance to level 2! ")
else:
    print("please try again! ")

Question_2 = input("What does RAM stand for? ")
if Question_2 == "Random Access Memory":
    print("good job! you can advance to level 3! ")
else:
    print("please try again! ")

Question_3 = input("What does GB stand for? ")
if Question_3 == "GigaByte":
    print("good job! you can advance to level 4! ")
else:
    print("please try again! ")

Question_4 = input("What does GPU stand for? ")
if Question_4 == "Graphics Processing Unit":
    print("good job! you can advance to level 5! ")
else:
    print("please try again! ")
