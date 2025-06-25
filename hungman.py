import random

# 1. Predefined list of 5 words
words = ["apple", "tiger", "zebra", "chair", "plane"]

# 2. Randomly select a word
secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_wrong_guesses = 6

# 3. Create a display version of the word (e.g., _ _ _ _ _)
display_word = ["_"] * len(secret_word)

print("🎮 Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses allowed.\n")

# 4. Main game loop
while wrong_guesses < max_wrong_guesses and "_" in display_word:
    print("Word:", " ".join(display_word))
    print("Guessed letters:", " ".join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print("❌ Please enter only a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter. Try a new one.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("✅ Correct guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                display_word[i] = guess
    else:
        wrong_guesses += 1
        print(f"❌ Wrong guess! Tries left: {max_wrong_guesses - wrong_guesses}\n")

# 5. End of game
if "_" not in display_word:
    print("🎉 You won! The word was:", secret_word)
else:
    print("😢 You lost! The correct word was:", secret_word)
