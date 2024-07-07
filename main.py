

print("Greetings, mere mortal. You\'re here for the escape room, aren't ya?")
print("""Well, the Escape room is no easy task, let me tell ya. The first few levels are of average difficulty, but don\'t let that fool ya.""")
print("The Blade of Deception, you\'re here for it. Legend has it that the Blade of Deception was crafted by the 3 cosmic warlords to defeat Evan, a corrupted being cursed with the power to destroy, but no one has seen him for centuries.")
tutorials = input("You\'re given the chance to acquire the blade, but nobody said this would be easy. It may even cost your life, to prepare you, there is a pratice room, so do you need it? (in/out)")

if tutorials == "in":
  import tutorial
if tutorials == "out":  
  print("You run for the exit, but find the door locked. You are trapped.")
  print("You see a small window, but it\'s too high to reach. You need to play.")
  level = input("Seclect your level from 1 to 10: ")

  if level == "1":
   import level1
  if level == "2":
    import level2
  if level == "3":
    import level3
  if level == "4":
    import level4
  if level == "5":
    import level5  
  if level == "6":
   import level6
  if level == "7":
    import level7
  if level == "8":
   import level8
  if level == "9":
    import level9
  if level == "10":
   import level10