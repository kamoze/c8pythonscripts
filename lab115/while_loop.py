# Print statements
print("Welcome to Guess The Number!")
print("The rules are simple. I will think of a number and you try to guess it.")
# Import modules here
import random

#variables here
number = random.randint(1, 10)
print(number)

isGuessRight = False

# while loop starts here
while isGuessRight != True:
  guess = input("Guess a number between 1 and 10: ")
  if int(guess) == number:
    print("You guessed {}. That is right! You win!".format(guess))
    isGuessRight = True
  else:
    print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))