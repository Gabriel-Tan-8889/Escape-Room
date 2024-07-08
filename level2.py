import time

print("System: Welcome to Level 2. Good Luck!")

print("System: Welcome to alien room part 1. In this room, you will have to answer a series of questions to pass. If you get one wrong, we will take your memory")

q1 = input("System: Question 1: What is the capital of France?")

if q1 == "Paris":
  print("System: Correct! Next Question.")
  q2 = input("System: Question 2: Who is harry potter's wife? A) Ginny Weasley B) Cho Chang C) Lily Evans")
  if q2 == "A":
    print("System: Correct! Next Question.")
    q3 = input("System: Question 3: Who is the skipper of the heron? A) Hal B) Stig C) Bill")
    if q3 == "A":
      print("System: Correct! Next Question.")
      q4 = input("Last Question: Who is known for doing his own stunts? A) Tom Cruise B) Tom Hanks C) Tom Holland")
      if q4 == "A":
        print("System: Correct! Congratulations.")
        print("System: Sending you back to earth.")
        time.sleep(3)
        continu = input("Do you want to continue?")
        if continu == "yes":
          import level3
        elif continu == "no":
          import main
        else:
          print("System: Incorrect. Stay still.")
          time.sleep(5)
          print("Memory wipe completed. You have been taken back to the start.")
          import main
      else:
        print("System: Incorrect. Stay still.")
        time.sleep(5)
        print("Memory wipe completed. You have been taken back to the start.")
        import main
    else:
      print("System: Incorrect. Stay still.")
      time.sleep(5)
      print("Memory wipe completed. You have been taken back to the start.")
      import main
  else:
    print("System: Incorrect. Stay still.")
    time.sleep(5)
    print("Memory wipe completed. You have been taken back to the start.")
    import main
else:
  print("System: Incorrect. Stay still.")
  time.sleep(5)
  print("Memory wipe completed. You have been taken back to the start.")
  import main