import random

ROCK="r"
SCISSORS="s"
PAPER="p"
emojis ={ROCK:"🥌",SCISSORS:"✂",PAPER:"📃"}

choices=tuple(emojis.keys())

def user_choice():
    while True:
        user_input=input("Rock,paper, or scissors? (r/p/s): ").lower()
        if user_input in choices:
            return user_input        
        else:
            print("Invalid choice!")

def display_choices(user_input,computer_choice):    
    print(f"You chose {emojis[user_input]}")
    print(f"Computer chose {emojis[computer_choice]}")
    
def determine_winner(user_input,computer_choice):
    if user_input==computer_choice:
        print("Tie!")
    elif (
        (user_input =="ROCK" and computer_choice =="SCISSORS") or
        (user_input =="SCISSORS" and computer_choice=="PAPER") or 
        (user_input =="PAPER" and computer_choice=="ROCK")):
        print("You win!")
    else:
        print("You lose!")
   
def play_game():             
    while True:
        user_input=user_choice()            
        computer_choice = random.choice(choices)        
        display_choices(user_input,computer_choice)        
        determine_winner(user_input,computer_choice) 
               
        should_continue=input("Continue (y/n): ").lower()
        if should_continue=="n":
            print("The End!")
            break

play_game()