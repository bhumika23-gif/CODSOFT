import random

choices = ["rock", "paper", "scissors"]
user_score = 0
comp_score = 0

while True:
    user = input("\nChoose rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid input. Try again.")
        continue

    comp = random.choice(choices)
    print(f"Computer chose: {comp}")

    if user == comp:
        print("It's a tie!")
    elif (user == "rock" and comp == "scissors") or \
         (user == "scissors" and comp == "paper") or \
         (user == "paper" and comp == "rock"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        comp_score += 1

    print(f"Score - You: {user_score} | Computer: {comp_score}")
    
    again = input("Play again? (yes/no): ").lower()
    if again != 'yes':
        print("Thanks for playing!")
        break
