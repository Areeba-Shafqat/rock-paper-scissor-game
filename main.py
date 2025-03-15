import random

choices=["r","p","s"]
emojis ={"r":"🥌","s":"✂","p":"📃"}

while True:
    user_input=input("Rock,paper, or scissors? (r/p/s): ").lower()
    if user_input not in choices:
        print("Invalid choice!")
        continue
        
    computer_choice = random.choice(choices)

    print(f"You chose {emojis[user_input]}")
    print(f"Computer chose {emojis[computer_choice]}")

    if user_input==computer_choice:
        print("Tie!")
    elif (
        (user_input =="r" and computer_choice =="s") or
        (user_input=="s" and computer_choice=="p") or 
        (user_input=="p" and computer_choice=="r")):
        print("You win!")
    else:
        print("You lose!")
        
    should_continue=input("Continue (y/n): ").lower()
    if should_continue=="n":
        print("The End!")
        break