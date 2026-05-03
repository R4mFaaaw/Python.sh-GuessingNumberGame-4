import random
import time

def start_game():
    print("\nWelcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # 1. Pilih Tingkat Kesulitan
    print("\nPlease select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    
    choice = input("\nEnter your choice (1-3): ")
    
    levels = {
        "1": ("Easy", 10),
        "2": ("Medium", 5),
        "3": ("Hard", 3)
    }
    
    if choice not in levels:
        print("Invalid choice! Defaulting to Medium.")
        choice = "2"
        
    level_name, chances = levels[choice]
    print(f"\nGreat! You have selected the {level_name} difficulty level.")
    print("Let's start the game!")

    # 2. Inisialisasi Angka Acak dan Waktu
    secret_number = random.randint(1, 100)
    attempts = 0
    start_time = time.time()

    # 3. Loop Permainan
    while attempts < chances:
        try:
            guess = int(input("\nEnter your guess: "))
            attempts += 1
            
            if guess == secret_number:
                end_time = time.time()
                duration = round(end_time - start_time, 2)
                print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
                print(f"It took you {duration} seconds.")
                return attempts # Mengembalikan skor
            
            elif guess < secret_number:
                print(f"Incorrect! The number is greater than {guess}.")
            else:
                print(f"Incorrect! The number is less than {guess}.")
                
            remaining = chances - attempts
            if remaining > 0:
                print(f"You have {remaining} chances left.")
            
        except ValueError:
            print("Please enter a valid number!")

    print(f"\nGame Over! You've run out of chances. The number was {secret_number}.")
    return None

def main():
    while True:
        start_game()
        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()