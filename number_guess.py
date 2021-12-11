import random

range_of_number=input("Enter the number: ")

if range_of_number.isdigit():
     range_of_number=int(range_of_number)

     if range_of_number<=0:
          print("Please enter a number greater than 0 next time.")
          quit()
else:
     print("Please type number next time")     
random_number=random.randrange(0, range_of_number)
guess_count=0

while True:
     guess_count+=1
     user_guess = input("Make a guess: ")
     if user_guess.isdigit():
          user_guess = int(user_guess)
     else:
          print('Please type a number next time.')
          continue

     if user_guess == random_number:
          print("Hurry You got it!")
          break
     elif user_guess > random_number:
          print("You were above the number!")
     else:
          print("You were below the number!")

print("You got it in", guess_count, "guesses")
