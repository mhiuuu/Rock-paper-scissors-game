import random

while True:
  choices = ["rock", "paper", "scissors"]

  computer = random.choice(choices)
  player = input("rock, paper or scissors?: ").lower()

  while player not in choices:
    player = input("Stop joking!Be serious. Rock - paper - scissors?:").lower()

  if player == computer:
    print("One two three, rock - paper - scissors!")
    print("Player choosed: " + player)
    print("Your opponent choosed: " + computer)
    print("TIEEEE")
  
  elif player == "rock":
    if computer == "scissors":
      print("One two three, rock - paper - scissors!")
      print("Player choosed: " + player)
      print("Your opponent choosed: " + computer)
      print("YOU WINNNN!!!")   
    elif computer == "paper":
      print("One two three, rock - paper - scissors!")
      print("Player choosed: " + player)
      print("Your opponent choosed: " + computer)
      print("YOU LOSE....")
  
  elif player == "scissors":
    if computer == "paper":
      print("One two three, rock - paper - scissors!")
      print("Player choosed: " + player)
      print("Your opponent choosed: " + computer)
      print("YOU WINNNN!!!")    
    elif computer == "rock":
      print("One two three, rock - paper - scissors!")
      print("Player choosed: " + player)
      print("Your opponent choosed: " + computer)
      print("YOU LOSE....")
  
  elif player == "paper":
    if computer == "rock":
      print("One two three, rock - paper - scissors!")
      print("Player choosed: " + player)
      print("Your opponent choosed: " + computer)
      print("YOU WINNNN!!!")
    elif computer == "scissors":
      print("One two three, rock - paper - scissors!")
      print("Player choosed: " + player)
      print("Your opponent choosed: " + computer)
      print("YOU LOSE....")
