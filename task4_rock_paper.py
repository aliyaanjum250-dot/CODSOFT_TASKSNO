import random

choices = ["rock", "paper", "scissors"]

print("===== ROCK PAPER SCISSORS =====")

user_score = 0
computer_score = 0

while True:
    user = input("Enter rock, paper, scissors or quit: ").lower()

    if user == "quit":
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print("Your score:", user_score)
    print("Computer score:", computer_score)

print("\n===== FINAL SCORE =====")
print("Your score:", user_score)
print("Computer score:", computer_score)
print("Game over!")