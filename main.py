import random
from art import logo

print (logo)
hard_level = 5
easy_level = 10

correct_number = random.randint(1,100)
# print(correct_number)
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a Difficulty. type 'easy' or 'hard': ")

# Difficulty level
def set_dificulty():
 
  if difficulty == "easy":
    return easy_level
  else:
    return hard_level

    


def play_game():

  diff = set_dificulty()

  print(f"You have {diff} attempts to guess the number.")

  correct_guess = False 

  while not correct_guess:
    
    player_guess = int(input("Make a guess: "))
    if player_guess > correct_number:
      print("Too high")
      if player_guess != correct_number:
        # diff is the difficulty level and live
        diff -= 1 

        print(f"you have {diff} live(s) left")
        if diff == 0:
          print("Game over")
          correct_guess = True
    elif player_guess < correct_number:
      print("Too low")
      if player_guess != correct_number:
        diff -= 1
        print(f"you have {diff} live(s) left")
        if diff == 0:
          print("Game over")
          correct_guess = True
    if player_guess == correct_number:
      print(f"correct guess, the number was {correct_number}")
      correct_guess = True


play_game()

  