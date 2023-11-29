import random

def choose_word():
    words = ["weed", "monkey", "football", "basketball", "KFC", "Popeyes", "alexidol"]
    return random.choice(words)

def display_word(word, guessed_word)
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def hangman():
    words = ['python', 'hangman', 'programming', 'challenge', 'coding']
    word_to_guess = random.choice(words).lower()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(word_to_guess, guessed_letters))

    while '_' in display_word(word_to_guess, guessed_letters) and attempts > 0:
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        guessed_letters.add(guess)

        if guess not in word_to_guess:
            attempts -= 1
            print(f"Incorrect! Attempts left: {attempts}")
        else:
            print("Correct!")

        print(display_word(word_to_guess, guessed_letters))

    if '_' not in display_word(word_to_guess, guessed_letters):
        print("Congratulations! You guessed the word.")
    else:
        print(f"Sorry, you ran out of attempts. The word was '{word_to_guess}'.")

if __name__ == "__main__":
    hangman()
