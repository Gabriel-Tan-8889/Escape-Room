print("Welcome to Level 5. Good Luck!")

print("System: Your job is to kill Lucas Khaw.")
print("System: He is a Malaysian with dark hair and wears glasses like Harry Potter.")
print("System: You get to choose how you kill him.")
print("System: You can either kill him with a knife or with a gun.")
print("System: You can also choose to kill him with a bomb.")

choice = input("System: Choose your weapon (knife, gun, bomb): ")
print("System: You chose to kill Lucas with a", choice)
print("good luck")
print("System: Releasing Lucas Khaw")

if choice == "knife":
  print("Your try to stab him but he dodges it and takes the knife out of your hand and stabs you. You start to bleed out.")
  time.sleep(5)
  print("System: Level Failed. Try again.")
  import main
elif choice == "gun":
  print("You shoot him in the head and he dies. You are saved")
  print("System: Level passed. Congratulations!")
  import level6
if choice == "bomb":
  print("While the system releases Lucas, you quickly throw a bomb in the area he is held at and plant another at the entrance")
  print("When the bomb explodes, he stumbles around and step on the bomb on the floor and it kills him. You are saved")
  print("System: Level passed. Congratulations!")
  import level6