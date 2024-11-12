import random

# Function to set up the game based on difficulty
def set_difficulty():
    print("Choose difficulty level:")
    print("1. Easy (1-10, 5 attempts)")
    print("2. Medium (1-50, 7 attempts)")
    print("3. Hard (1-100, 10 attempts)")
    choice = input("Enter choice (1/2/3): ")
    
    if choice == '1':
        return 10, 5  # Range 1-10, 5 attempts
    elif choice == '2':
        return 50, 7  # Range 1-50, 7 attempts
    elif choice == '3':
        return 100, 10  # Range 1-100, 10 attempts
    else:
        print("Invalid choice. Defaulting to Easy level.")
        return 10, 5  # Default to Easy level

# Function to play the game
def play_game():
    # Set up difficulty
    upper_limit, max_attempts = set_difficulty()
    
    # Generate a random number in the chosen range
    number_to_guess = random.randint(1, upper_limit)
    
    print(f"\nI'm thinking of a number between 1 and {upper_limit}. You have {max_attempts} attempts to guess it!")
    
    # Loop for the user's guesses
    attempts_left = max_attempts
    while attempts_left > 0:
        # Get the user's guess and validate the input
        try:
            guess = int(input(f"\nYou have {attempts_left} attempts left. Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        # Check if the guess is correct, too high, or too low
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
            break
        
        # Decrease the number of attempts left
        attempts_left -= 1
    
    # If out of attempts, reveal the correct number
    if attempts_left == 0:
        print(f"Sorry, you're out of attempts. The correct number was {number_to_guess}.")
    
    # Ask if the user wants to play again
    play_again = input("\nDo you want to play again? (y/n): ")
    if play_again.lower() == 'y':
        play_game()
    else:
        print("Thanks for playing! Goodbye.")

# Start the game
if __name__ == "__main__":
    play_game()
