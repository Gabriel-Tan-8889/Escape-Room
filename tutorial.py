print("System: Tutorial selected. Good Luck!")

print("Narrator: You are in a dark room with a locked door.")
print("Narrator: You see a key on the table.")
print("Narrator: What do you want to do?")
choice = input("Type 'take key' or 'open door': ")
if choice == "take key":
  print("Narrator: You take the key and unlock the door.")
  opendoor = input("Do you want to open the door?")
if opendoor == "yes":
                   print("Narrator: Congagulations. You have passed the tutorial.")
                   continuing = input("do you want to continue?")
                   if continuing == "yes":
                     import level1
                   if continuing == "no":
                     import main
if opendoor == "no":
                  print("Narrator: There is a cabinet in the room. You open it and find a note.")
                  print("Narrator: The note says: 'The door is locked. Use the key.''")
                  print("Narrator: Level Failed. Try again")
                  import main
if choice == "open door":
  print("Narrator: The door is locked. You need a key.")
  takekey == input("Do you want to take the key?")
  if takekey == "yes":
    print("Narrator: You take the key and unlock the door.")
    opendoor = input("Do you want to open the door?")
    if opendoor == "yes":
                   print("Narrator: Congagulations. You have passed the turtorial.")
                   continuing = input("do you want to continue?")
                   if continuing == "yes":
                     import level1
                   if continuing == "no":
                     import main
    if opendoor == "no":
                  print("Narrator: There is a cabinet in the room. You open it and find a note.")
                  print("Narrator: The note says: 'The door is locked. Use the key.''")
                  print("Narrator: Level Failed. Try again")
                  import main
  if takekey == "no":
    print("Narrator: You are stuck in the room forever.")
    wait = input("Do you want to wait?")
    if wait == "yes":
      print("Narrator: You wait for hours and hours and hours. You die of starvation.")
      print("Narrator: Level Failed. Try again")
      import main
    if wait == "no":
      print("Narrator: You are stuck in the room forever.")
      print("Narrator: Level Failed. Try again")
      import main