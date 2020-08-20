# Snake Water Game  in Python

import random
l1 = [ "Snake" , "Water" , "Gun"]
print("Press s for snake")
print("Press w for water")
print("Press g for gun")
lose_matches = 0
won_matches = 0
for num in range(0,10):
       user_no = input("Enter your number\n ")
       print("Enteres choice : ", user_no)
       random_no = random.choice(l1)
       print("Computer choose : " ,random_no )
       if user_no=="s" and random_no=="Water":
           print("You Loose")
           print(9-num , "chance left")
           # global lose_matches
           lose_matches = lose_matches+1

       elif user_no=="w" and random_no=="Water":
           print("Match Draw")
           print(9 - num, "chance left")
       elif user_no=="g" and random_no=="Water":
           print("You loose")
           print(9 - num, "chance left")
           # global lose_matches
           lose_matches = lose_matches + 1
       elif user_no=="s" and random_no=="Snake":
           print("Draw ")
           print(9 - num, "chance left")
       elif user_no=="w" and random_no=="Snake":
           print("You win ")
           print(9 - num, "chance left")
           # global won_matches
           won_matches = won_matches + 1
       elif user_no=="g" and random_no=="Snake":
           print("You Win ")
           print(9 - num, "chance left")
           # global won_matches
           won_matches = won_matches + 1
       elif user_no=="s" and random_no=="Gun":
           print("You lose ")
           print(9 - num, "chance left")
           # global lose_matches
           lose_matches = lose_matches + 1
       elif user_no=="w" and random_no=="Gun":
           print("You win")
           print(9 - num, "chance left")
           won_matches = won_matches + 1
       elif user_no=="g" and random_no=="Gun":
           print("Match Draw ")
           print(9 - num, "chance left")
       else:
           print("You enter wrong input")
           print(9 - num, "chance left")
num = num+1

print("Win matches : ", won_matches)
print("Loses mathes : ", lose_matches)


if won_matches>lose_matches:
    print("You win")
elif won_matches==lose_matches:
    print("Match is draw  , please try again")
else:
    print("You lose")
