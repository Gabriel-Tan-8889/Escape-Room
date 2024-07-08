import time
print("System: Welcome to Level 3. Good Luck!")

print("You are a dective and you are trying to find a killer")
print("You are in a room with a suspect, you have to find the killer")
print("There are 5 susupect Mandy, Josh, John, Lucas and Evan")

print("You ask each person where they were during the murder")
print("Mandy: I was at the party")
print("John: I was marking my students paper")
print("Lucas: I was at the gym")
print("Josh: I was at the bar eating blue cheese and white wine")
print( "Evan: I was at the football feild.")

personanswer = input("Who do you think is the killer?")

if personanswer == "Josh":
  print("You are correct. Congruagulations.")
  continu = input("Do you want to continue?")
  if continu == "yes":
    import level4
else:
  print("You are incorrect. The killer kills you soon after.")
  print("Heading to lobby")
  time.sleep(5)
  import main