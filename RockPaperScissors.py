import random

rock = '''
    ______
---'   ____)
      (_____)
      (_____)
      (____)
---._(___)

'''

paper = '''
     _______
---'     ____)____
            ______)
           _______)
          _______)
---.. __________)
'''
scissors= '''
    _______
---'    ____)____
           ______)
        __________)
      (____)
---.__(___)
'''
countU = 0
countC = 0
CountD = 0
choice = [rock, paper, scissors]
print("This is a simple Rock Paper Scissors game.")

def playGame():
    global countU
    global countC
    global CountD
    user_choice = int(input("Choose any one: \n0 : Rock\n1 : Paper\n2 : Scissors\n"))

    if user_choice > 2 or user_choice < 0:
        print("Invalid input, you lose")
        countC+=1
    else:
        if user_choice == 0:
            print("You chose ROCK!!\n")
        elif user_choice == 1:
            print("You chose PAPER!!\n")
        elif user_choice == 2:
            print("You chose SCISSORS!!\n")
        print(choice[user_choice])

        computer_choice = random.randint(0,2)
        if computer_choice == 0:
            print("Computer chose ROCK!!\n",)
        elif computer_choice == 1:
            print("Computer chose PAPER!!\n")
        elif computer_choice == 2:
            print("Computer chose SCISSORS!!\n")
        print(choice[computer_choice])

        if computer_choice == user_choice:
            print("It's a tie")
            CountD+=1
        elif computer_choice == 0 and user_choice == 1:
            print("You win")
            countU+=1
        elif computer_choice == 1 and user_choice == 2:
            print("You win")
            countU+=1
        elif computer_choice == 2 and user_choice == 0:
            print("You win")
            countU+=1
        else:
            print("You lose!!!")
            countC+=1

playAgain = "y"

while playAgain == "y":
    playGame()
    playAgain = (input("Play again? (Y or N)\n")).lower()

totalCount = countU+countC+CountD
print(f"GAME OVER. After {totalCount} attempts, you won {countU} time(s)")
