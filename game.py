"""
Perpetual Rock, Paper, Scissors, Lizard, Spock
"""
import random

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
lizard = "Lizard"
spock = "Spock"

options = {
  rock: [scissors, lizard],
  scissors: [paper, lizard],
  paper: [rock, spock],
  spock: [rock, scissors],
  lizard: [paper, spock],
}

choices = list(options.keys())

while True:
  user_hand = ""

  while True:
    user_hand = input(f"Choose from {', '.join(choices)}: ")
    if (user_hand not in choices):
      print(f"Incorrect choice. You can only choose from {', '.join(choices)}")
    else:
      break

  enemy_hand = random.choice(choices)

  print(f"\nYou play {user_hand}...")
  print(f"Opponent plays {enemy_hand}...\n")

  result = ""
  if (user_hand == enemy_hand):
    result = "Tie 🤝"
  else:
    if (enemy_hand in options.get(user_hand)):
      result = "You win! 🙌"
    else:
      result = "You lost! 😿"

  print(result)
  print("—————————————\n")
