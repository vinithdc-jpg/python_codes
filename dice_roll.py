import random

while True:
    print("Dice:", random.randint(1, 6))
    again = input("Roll again? (y/n): ")

    if again.lower() != "y":
        break