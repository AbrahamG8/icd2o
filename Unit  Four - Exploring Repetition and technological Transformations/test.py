import random
 
def choose_word():
    words = ["monkey", "football", "weed", "chicken", "watermelon", "rock", "pock"]
    return random.choice(words)
 
def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display
 
def is_lowercase_letter(char):
    return 'a' <= char <= 'z'
 
def hangman():
    print("Welcome to Hangman!")
    word_to_guess = choose_word()
    guessed_letters = []
    attempts = 10
 
    while attempts > 0:
        current_display = display_word(word_to_guess, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Attempts left: {attempts}")
 
        guess = input("Guess a letter: ").lower()
 
        if len(guess) != 1 or not is_lowercase_letter(guess):
            print("Please enter a valid single letter.")
           
 
        if guess not in guessed_letters:
            guessed_letters.append(guess)
        else:
            print("You've already guessed that letter. Try again.")
           
 
        if guess not in word_to_guess:
            print("Incorrect guess!")
            attempts -= 1
        else:
            print("Correct guess!")
 
        if set(guessed_letters) == set(letter for letter in word_to_guess):
            print("Congratulations! You've guessed the word:", word_to_guess)
            break
 
        if attempts == 0:
            print("Sorry, you've run out of attempts. The word was:", word_to_guess)
 
if __name__ == "__main__":
    hangman()