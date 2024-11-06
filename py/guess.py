import random

number = random.randint(1, 100)
chances = int(input("Enter number of chances: "))

while chances > 0 and (guess := int(input(f"Guess (1-100), {chances} left: "))) != number:
    print("Too high!" if guess > number else "Too low!")
    chances -= 1

print("Congratulations! You guessed it!" if guess == number else f"Out of chances! The number was {number}.")
