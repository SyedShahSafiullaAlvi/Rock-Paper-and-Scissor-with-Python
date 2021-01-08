
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''' 

# function for the game
def game(user_points,python_points):
    import random           # to randomize choice of python each time
    import time             # to make the user wait for n seconds before showing python's choice

    while 1:
        # Asking the user to choice between Rock Paper and Scissor
        user_choice=input("R for ROCK\nP for PAPER\nS for SCISSOR\nEnter your choice: ").upper()     
        print("Your choice....")

        if user_choice=='R':              # if user chooses Rock, print Rock 
            print(rock)
            break
        elif user_choice=='P':           # if user chooses Paper, print Paper 
            print(paper)
            break
        elif user_choice=='S':          # if user chooses scissor, print scissor 
            print(scissor)
            break
        else:                           # or else ask user to enter again the choice
            print("Invalid chioice!!")
            continue

    # PYTHON's choice
    python_choice=random.choice(['R','P','S'])          
    print("Python choice is...")
    time.sleep(3)                       # amaking the user to wait for 3 seconds to maintain excitement

    if python_choice=='R':          # if python randomly chooses Rock, print Rock 
        print(rock)

    elif python_choice=='P':        # if python randomly chooses paper, print paper 
        print(paper)

    elif python_choice=='S':        # if python randomly chooses scissor, print scissor 
        print(scissor)
        

    # Now checking, with respect to rules of game
    if user_choice=='R' and python_choice=='P':
        print("You lose!")
        python_points+=1
        print(user_points,python_points)

    elif user_choice=='R' and python_choice=='S':
        print("You win!")
        user_points+=1
        print(user_points,python_points)

    elif user_choice=='P' and python_choice=='R':
        print("You win!")
        user_points+=1
        print(user_points,python_points)

    elif user_choice=='P' and python_choice=='S':
        print("You lose!")
        python_points+=1
        print(user_points,python_points)

    elif user_choice=='S' and python_choice=='P':
        print("You win!")
        user_points+=1
        print(user_points,python_points)

    elif user_choice=='S' and python_choice=='R':
        print("You lose!")
        python_points+=1
        print(user_points,python_points)

    elif user_choice==python_choice:
        print("Its a Tie!")
    



user_points,python_points=0,0
name=input("What's your name? ")                # prompting user to enter name

print(f"Hey {name}, PYTHON here. Lets play Rock Paper Scissor ")       

# asking user whether he/she want to play with points or without points
format=input("You wanna play with points or without points? Type 'P' to play points or else type 'W' : ")   


while 1:
    if format=='P':             # play with points
        game(user_points,python_points)
        while 1:
            play_again=input("You wanna play again? Type 'S' to play again or else type 'N': ")
            if play_again=='S':
                game(user_points,python_points)
                continue
            elif play_again=='N':
                break
            else:
                print("Invalid choice!!")
                continue

    elif format=='W':           # play without points
        game(user_points,python_points)

    else:                   # if anything else is typed, asks user to enter again between 'P' and 'W'
        print("Invalid choice!!")
        continue

# RESULT
if user_points > python_points:         
    print("Finally You won")
elif user_points > python_points:
    print("Finally You lose")