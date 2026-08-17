import random


def game_win(user, computer):
    if user == computer:
        return "tie"
    if (
        (user == "snake" and computer == "water")
        or (user == "water" and computer == "gun")
        or (user == "gun" and computer == "snake")
    ):
        return "user"
    return "computer"

random_number = random.randint(1, 3)
print("computer choice is: snake (1), water (2), gun (3)")
if random_number == 1:
    computer_choice = "snake"
elif random_number == 2:
    computer_choice = "water"
else:
    computer_choice = "gun"

user_choice = input("Enter your choice (snake, water, gun): ").lower()

result = game_win(user_choice, computer_choice)
print(f"Computer choice: {computer_choice}")
print(f"User choice: {user_choice}")

if result == "tie":
    print("It's a tie!")
elif result == "user":
    print("Congratulations! You win!")
else:
    print("Sorry, you lose. Better luck next time!")

