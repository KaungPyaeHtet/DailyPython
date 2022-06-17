from random import randint
import math

lower = int(input("Lower: "))
upper = int(input("Upper: "))
answer = randint(lower, upper)
count = 0
chances = int(math.log(upper - lower + 1, 2))
print("You have {} chances to guess the number\n".format(chances))

while chances > count:
    try:
        print("--------------------------------------------------")
        guess = int(input(f"Guess a number between {lower} to {upper}: "))
        if guess == answer:
            print("Congrats, you won in {} guess".format(count))
            break
        elif guess < answer:
            print("You guessed too low")
        elif guess > answer:
            print("You guessed too high")
        count += 1
    except ValueError:
        print("Enter a valid integer\n")
        continue

if count == chances:
    print("The number is {}".format(answer))
    print("Better luck next time")