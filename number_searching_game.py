import random

# ============================================
# NUMBER SEARCHING GAME
# A Beginner-Friendly Python Console Game
# ============================================

def clear_screen():
    """Clear the console screen"""
    print("\n" * 50)

def display_menu():
    """Display the main menu"""
    print("\n" + "=" * 50)
    print("🎮 WELCOME TO NUMBER SEARCHING GAME 🎮".center(50))
    print("=" * 50)
    print("\n1. 🎮 Start Game")
    print("2. ❌ Exit Game")
    print("\n" + "=" * 50)

def get_main_choice():
    """Get user choice from main menu"""
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        # Check if input is valid
        if choice in ['1', '2']:
            return choice
        else:
            print("❌ Invalid choice! Please enter 1 or 2.")

def display_difficulty_menu():
    """Display difficulty level selection"""
    print("\n" + "=" * 50)
    print("SELECT DIFFICULTY LEVEL".center(50))
    print("=" * 50)
    print("\n1. 🟢 Easy   (1-100, 10 tries)")
    print("2. 🔴 Hard   (1-250, 5 tries)")
    print("\n" + "=" * 50)

def get_difficulty_choice():
    """Get user choice for difficulty level"""
    while True:
        choice = input("\nEnter your choice (1 or 2): ").strip()
        
        if choice in ['1', '2']:
            return choice
        else:
            print("❌ Invalid choice! Please enter 1 or 2.")

def get_valid_guess(min_num, max_num):
    """Get and validate user guess"""
    while True:
        try:
            guess = input(f"\nEnter your guess ({min_num}-{max_num}): ").strip()
            
            # Convert to integer
            guess_num = int(guess)
            
            # Check if guess is within range
            if guess_num < min_num or guess_num > max_num:
                print(f"❌ Please enter a number between {min_num} and {max_num}!")
                continue
            
            return guess_num
        
        except ValueError:
            # Handle non-numeric input
            print("❌ Invalid input! Please enter a valid number.")

def calculate_score(max_tries, remaining_tries, max_score):
    """Calculate score based on tries remaining"""
    # Score is higher when fewer tries are used
    # Formula: (remaining_tries / max_tries) * max_score
    score = int((remaining_tries / max_tries) * max_score)
    
    # Ensure score doesn't go negative
    if score < 0:
        score = 0
    
    return score

def play_game(difficulty):
    """Main game logic"""
    
    # Set game parameters based on difficulty
    if difficulty == '1':  # Easy
        min_num = 1
        max_num = 100
        max_tries = 10
        max_score = 100
        level_name = "🟢 EASY"
    else:  # Hard
        min_num = 1
        max_num = 250
        max_tries = 5
        max_score = 100
        level_name = "🔴 HARD"
    
    # Generate random hidden number
    hidden_number = random.randint(min_num, max_num)
    
    # Game variables
    tries_remaining = max_tries
    guessed = False
    
    # Display game start message
    print("\n" + "=" * 50)
    print(f"🎯 GAME STARTED - {level_name} LEVEL".center(50))
    print("=" * 50)
    print(f"\n📊 I have hidden a number between {min_num} and {max_num}.")
    print(f"🎯 You have {max_tries} tries to find it!\n")
    
    # Game loop
    while tries_remaining > 0 and not guessed:
        # Show remaining tries
        print(f"⏳ Tries Remaining: {tries_remaining}")
        
        # Get player's guess
        guess = get_valid_guess(min_num, max_num)
        
        # Check the guess
        if guess == hidden_number:
            guessed = True
            print("\n" + "🎉" * 25)
            print("🎉 CONGRATULATIONS! YOU FOUND THE NUMBER! 🎉".center(50))
            print("🎉" * 25)
            
            # Calculate and display score
            score = calculate_score(max_tries, tries_remaining, max_score)
            print(f"\n✨ Your Score: {score} points")
            print(f"🏆 Tries Used: {max_tries - tries_remaining} out of {max_tries}")
            
        elif guess < hidden_number:
            print(f"⬆️  Too Low! The hidden number is HIGHER than {guess}.")
            tries_remaining -= 1
            
        else:  # guess > hidden_number
            print(f"⬇️  Too High! The hidden number is LOWER than {guess}.")
            tries_remaining -= 1
    
    # Game over - ran out of tries
    if not guessed:
        print("\n" + "❌" * 25)
        print("❌ GAME OVER! YOU RAN OUT OF TRIES! ❌".center(50))
        print("❌" * 25)
        print(f"\n📍 The hidden number was: {hidden_number}")
        print("💪 Try again with a better strategy!")
    
    return guessed

def ask_play_again():
    """Ask if player wants to play again"""
    while True:
        choice = input("\n🔄 Do you want to play again? (Y/N): ").strip().upper()
        
        if choice in ['Y', 'YES']:
            return True
        elif choice in ['N', 'NO']:
            return False
        else:
            print("❌ Invalid choice! Please enter Y or N.")

def exit_game():
    """Display exit message"""
    print("\n" + "=" * 50)
    print("👋 Thank you for playing Number Searching Game! 👋".center(50))
    print("=" * 50)
    print("\n✨ Keep practicing and improve your number guessing skills!")
    print("💯 See you next time! 💯\n")

def main():
    """Main game loop"""
    
    while True:
        # Display main menu
        display_menu()
        
        # Get user choice
        choice = get_main_choice()
        
        # Exit game
        if choice == '2':
            exit_game()
            break
        
        # Start game
        elif choice == '1':
            # Ask for difficulty level
            display_difficulty_menu()
            difficulty = get_difficulty_choice()
            
            # Play the game
            play_game(difficulty)
            
            # Ask if player wants to play again
            if not ask_play_again():
                exit_game()
                break

# ============================================
# START THE GAME
# ============================================

if __name__ == "__main__":
    main()
