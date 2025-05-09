import random

def number_guessing_game():
   guess_number=random.randint(1,100)
   max_tries=8
   tries=0

   print("Welcome to the Number Guessing Game!")
   print("I have selected a number between 1 and 100. Try to guess it.")
   print(f"you have {max_tries} maximum tries")

   while tries < max_tries:
      try:
         
         guess=int(input("Enter your number:"))
         tries +=1
         if guess < guess_number:
            print("Higher")

         elif guess>guess_number: 
            print("lower")

         else:
            print(f"congratutry: you gussed it in {tries} tries")
            break

      except ValueError:
         
         print("please! Enter a valid number.")
   else:
      print(f"Sorry, you've used all {max_tries} tries. The number was {guess_number}.")

number_guessing_game()    

