import time
import random
print("Level 2 selected. Good Luck!")

print("Speaker: Welcome to Wonka's escape room. Your goal is to escape the room. You will be given a series of choices. Choose wisely.")
print("Speaker: Your goal to to send a chocloate bar through the TV to MR Wonka in the other room. Good Luck!")




print("Spaker: You see all the ingridents in the world infront of you, chocolate, flour, sugar, bread, soup, cake, milk, strawberry, vanilla, eggs. You have to choose the right ingredients to make a chocloate bar.")




def check_ingredients(chosen_ingredients, correct_ingredients):
      """Checks if all chosen ingredients are correct.

      Args:
        chosen_ingredients: A list of ingredients the player chose.
        correct_ingredients: A list of correct ingredients for the puzzle.

      Returns:
        True if all chosen ingredients are correct, False otherwise.
      """
      if len(chosen_ingredients) != len(correct_ingredients):
          return False  # Number of ingredients doesn't match
      for i in range(len(correct_ingredients)):
          if chosen_ingredients[i].lower() != correct_ingredients[i].lower():
              return False  # Ingredient at this index is incorrect
      return True  # All ingredients are correct

  # Example usage:
  # Define the ingredients for the puzzle
ingredients = ["Chocolate", "Sugar", "Flour", "Milk"]
correct_ingredients = ingredients

  # Get the player's chosen ingredients (e.g., using input() or from a game interface)
chosen_ingredients = []
for i in range(len(correct_ingredients)):
      chosen_ingredients.append(input(f"Choose ingredient {i+1}: "))

  # Check if the chosen ingredients are correct
if check_ingredients(chosen_ingredients, correct_ingredients):
      print("Speaker: Correct! You chose all the right ingredients.")
      print("Speaker: A chocloate bar is made. All you need to do is to send it to MR Wonka.")
deliver = input("How do you deliver it? Run or the TV")
if deliver == "run":
      print("Speaker: Did you not read the instructions? Your goal to to send a chocloate bar through the TV to MR Wonka")
      print("System: Level Failed. Try again.")
import main
if deliver == "TV":
  print("Speaker: Well done! You have sent the chocloate bar to MR Wonka. He is very happy.")
  print("System: Level passed. Congratulations!")
  continuing = input("do you want to continue?")
if continuing == "yes":
     import level3
if continuing == "no":
     import main
else:
    print("Incorrect. Try again.")