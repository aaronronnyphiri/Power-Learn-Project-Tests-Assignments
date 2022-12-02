#   Write a Python program to guess a number between 1 to 9.
#   Note : User is prompted to enter a guess. If the user guesses wrong then the prompt appears 
#   again until the guess is correct, on successful guess, user will get a "Well guessed!" message, 
#   and the program will exit.
 
print("-------------------------------- GUESS THE NUMBER --------------------------------------")
print("How To Play : A number between 1 to 9 is hidden. You are required to guess what it is.")
print("Enjoy The Game.")
print("========================================================================================")
num = range(1,9)                                # num == range of values for guess validity
import random
s_num = random.randint(1,9)                     # Our secret number == s_num (program picks a different number everytime randomly )
guess = int(input("Guess the secret number from numbers between 1 to 9 : "))
while guess != s_num :
    if guess not in num :                       #For guesses outside the chosen range of numbers
        print("Sorry! You are out of range.")
        guess = int(input("Guess the secret number from numbers between 1 to 9 : "))
    else :                                      #For wrong choices
        print("Sorry! Wrong Number. Try again.")
        guess = int(input("Guess the secret number from numbers between 1 to 9 : "))

if guess == s_num :                             #For correct choices
    print("Well Guessed !!")
    print("------------------------------------- THE END ------------------------------------------")

        


