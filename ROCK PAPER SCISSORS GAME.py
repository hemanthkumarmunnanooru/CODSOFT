import random
options = ["ROCK","PAPER","SCISSOR"]
computer_choice = random.choice(options)
user_choice = input("choose ROCK,PAPER or SCISSOR:")
print("you choose:", user_choice)
print("computer choose :",computer_choice)
if user_choice == computer_choice:
  print("it is tie")
elif user_choice == "ROCK" and computer_choice=="SCISSOR":
 print("you win")
elif user_choice == "PAPER" and computer_choice=="ROCK":
  print("you win")
elif user_choice == "SCISSOR" and computer_choice=="PAPER":
  print("you win")
else:
  print("computer win")