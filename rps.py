import random as rd

print("******************************\n"
      "WELCOME TO ROCK PAPER SCISSORS\n"
      "******************************\n")

plyrname = str(input(("Enter your player name:")))

print("Hello", plyrname+"!\n")

print("*******RULES*******\n"
      "* You will be playing against the Computer.\n"
      "* You can select how many rounds you would like to play, the one the most points wins at the end wins.\n"
      "* Enter 'a' for rock\n"
      "* Enter 'b' for paper\n"
      "* Enter 'c' for scissors\n"
      "******GOOD LUCK!*******\n")

no_rounds=int(input("How many rounds would you like to play?"))
rps_list = ["rock", "paper", "scissors"]

a = rps_list[0]
b = rps_list[1]
c = rps_list[2]

plyr_points = 0
cmpt_points = 0

for rounds in range(no_rounds):
    plyr_choice = str(input("Select rock,paper,scissors :"))
    cmpt_choice = rd.choice(rps_list)
    if plyr_choice == "a":
        print(plyrname,"chose rock.")
        if cmpt_choice == a:
            print("Computer chose rock. It's a draw!\n")
        elif cmpt_choice == b:
            print("Computer chose paper. Computer wins this round\n")
            cmpt_points += 1
        elif cmpt_choice == c:
            print("Computer chose scissors.",plyrname,"wins this round\n")
            plyr_points += 1

    elif plyr_choice == "b":
          print(plyrname, "chose paper.")
          if cmpt_choice == a:
                print("Computer chose rock.",plyrname,"wins this round\n")
                plyr_points += 1
          elif cmpt_choice == b:
                print("Computer chose paper. It's a draw!\n")
          elif cmpt_choice == c:
                print("Computer chose scissors. Computer wins this round\n")
                cmpt_points += 1

    elif plyr_choice == "c":
          print(plyrname, "chose scissors.")
          if cmpt_choice == a:
                print("Computer chose rock. Computer wins this round\n")
                cmpt_points += 1
          elif cmpt_choice == b:
                print("Computer chose paper.",plyrname,"wins this round\n")
                plyr_points += 1
          elif cmpt_choice == c:
                print("Computer chose scissors. It's a draw!\n")
    else:
          print("You got kicked out for being an idiot. Only Enter a,b or c\n")
          quit()

print(plyrname+"'s points =",plyr_points)
print("Computer's points =",cmpt_points)

if plyr_points > cmpt_points:
      print(plyrname,"won!")
elif cmpt_points > plyr_points:
      print("Computer won, Better luck next time!")
else:
      print("It's a draw!")

