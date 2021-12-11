import random
choices=["rock","paper","scissor"]

computer_wins=0
user_wins=0
while True:
     user_input=input("Type Rock/paper/scissor or Q to quit : ").lower()
     if user_input=="q":
          print("Thanks for playing")
          break
     if user_input not in choices:
          print("Please type Rock/paper/scissor or Q to quit")
          continue
     computer_input=random.choice(choices)
     print(f"You chose {user_input} and computer chose {computer_input}")
     if user_input==computer_input:
          print("It's a tie")
     elif user_input=="rock" and computer_input=="paper":
          print("Computer wins")
          computer_wins+=1
     elif user_input=="rock" and computer_input=="scissor":
          print("You win")
          user_wins+=1
     elif user_input=="paper" and computer_input=="rock":
          print("You win")
          user_wins+=1
     elif user_input=="paper" and computer_input=="scissor":
          print("Computer wins")
          computer_wins+=1
     elif user_input=="scissor" and computer_input=="rock":
          print("Computer wins")
          computer_wins+=1
     elif user_input=="scissor" and computer_input=="paper":
          print("You win")
          user_wins+=1
     print(f"Computer wins {computer_wins} times and you win {user_wins} times")
     print("Thanks for playing")

