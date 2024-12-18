name = input("Type your name: ")
print(f"Welcome", name, "to this adventure! ")

answer = input("You stand on the edge of a dark, sprawling forest, you must make a choice, You can go either into the mystic forest, set up camp, or turn back and leave the forest behind. ").lower()

if answer == "into the mystic forest" :
    answer = input("you come to a river, you can walk around it or swim across ")
    if answer == "swim" :
        print("you are brave! you swam across the river despite crocodiles")
    elif answer == "walk":
        print("you walked for many miles and then lost track of time and water.")
    else:
        print("not a valid option. You lose!")

elif answer == "set up camp":
    print("you decided to set up camp, do you want to hunt an animal or roast marshmellows?")
    if answer == "hunt":
        print("instead of hunting, you got hunted by a bear")
    elif answer == "roast":
        print("You roasted marshmellows and now enjoy the rest of the camping trip")
    else:
        print("not a valid option. You lose!")

else:
    print("you chose to leave the forest behind. Good Bye.")

print(f"thank you for trying, {name}")
