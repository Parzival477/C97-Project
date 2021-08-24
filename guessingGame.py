import random

print("Number Guessing Game")
randomNo = random.randint(1,9)
chances = 0
print("Guess a number from 1 to 9")
while chances <5:
    guess = int(input("Enter your guess: "))
    if guess == randomNo:
        print("Congratulation! You have won!")
        break
    elif guess < randomNo:
        print("Your guess is too low. Guess a higher number than", guess)
    else:
        print("Your guess is too high. Guess a lower number than", guess) 
    chances+= 1

if not chances < 5:
    print("Your guess is wrong. The right answer is", number)