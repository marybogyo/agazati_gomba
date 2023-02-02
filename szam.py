import random
def oszthato():
    vel = int(random.random() * 49) + 1
    print(f"I/A:\n\t A generált szám: {vel}")
    if (vel % 5 == 0):
        print("A szám öttel osztható!")
    elif (vel % 3 == 0):
        print("A szám hárommal osztható!")
    elif (vel % 5 == 0) and (vel % 3 == 0):
        print(f"I/B:\n\t A szám öttel és hárommal is osztható!")