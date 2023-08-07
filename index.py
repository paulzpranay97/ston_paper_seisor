import random

def get_player_choice():
    """
    Get the player's choice for the game (stone, paper, or scissors).
    """
    choice = input("Enter your choice (stone, paper, scissors): ").lower()
    while choice not in ["stone", "paper", "scissors"]:
        print("Invalid choice. Please choose from stone, paper, or scissors.")
        choice = input("Enter your choice (stone, paper, scissors): ").lower()
    return choice

def get_random_computer_choice():
    """
    Generate a random choice for the computer (stone, paper, or scissors).
    """
    return random.choice(["stone", "paper", "scissors"])

def determine_winner(player_choice, computer_choice):
    """
    Determine the winner of the game based on player's and computer's choices.
    """
    if player_choice == computer_choice:
        return "It's a tie!"
    if (player_choice == "stone" and computer_choice == "scissors") or \
       (player_choice == "scissors" and computer_choice == "paper") or \
       (player_choice == "paper" and computer_choice == "stone"):
        return "You win!"
    return "Computer wins!"

def main():
    """
    Main function to run the Stone-Paper-Scissors game.
    """
    print("Welcome to the Stone-Paper-Scissors game!")
    
    while True:
        player_choice = get_player_choice()
        computer_choice = get_random_computer_choice()
        
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")
        
        result = determine_winner(player_choice, computer_choice)
        print(result)
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            break
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
