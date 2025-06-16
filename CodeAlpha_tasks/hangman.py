import random

# ASCII art for each hangman stage
HANGMAN_PICS = [
    '''
     +---+
         |
         |
         |
        ===''',
    '''
     +---+
     O   |
         |
         |
        ===''',
    '''
     +---+
     O   |
     |   |
         |
        ===''',
    '''
     +---+
     O   |
    /|   |
         |
        ===''',
    '''
     +---+
     O   |
    /|\\  |
         |
        ===''',
    '''
     +---+
     O   |
    /|\\  |
    /    |
        ===''',
    '''
     +---+
     O   |
    /|\\  |
    / \\  |
        ==='''
]

# List of words to choose from
WORD_LIST = ['python', 'hangman', 'programming', 'code', 'developer', 'function']

def choose_word():
    return random.choice(WORD_LIST)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    word = choose_word()
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong = len(HANGMAN_PICS) - 1

    print("🎮 Welcome to Hangman!")
    
    while wrong_guesses < max_wrong:
        print(HANGMAN_PICS[wrong_guesses])
        print("Word:", display_word(word, guessed_letters))
        print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        
        guess = input("Guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("⚠️ Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("🔁 You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print("✅ Good guess!")
            if all(letter in guessed_letters for letter in word):
                print("\n🎉 You won! The word was:", word)
                break
        else:
            wrong_guesses += 1
            print("❌ Wrong guess!")

    if wrong_guesses == max_wrong:
        print(HANGMAN_PICS[wrong_guesses])
        print("\n💀 Game Over! The word was:", word)

if __name__ == "__main__":
    hangman()
