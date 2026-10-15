import random
print("🎮 Welcome to Hangman!")
print("guess the word!")
words=["python","developer","computer","coding","progaramer"]
word=random.choice(words)
hidden_word = ["_"] * len(word)
attempts = 5
guessed_letters = []
while attempts > 0 and "_" in hidden_word:
    print("Word:", " ".join(hidden_word))
    print("Attempts left:", attempts)

    guess = input("Guess a letter: ").lower().strip()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one letter only!")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")

        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
    else:
        print("Wrong guess!")
        attempts -= 1

if "_" not in hidden_word:
    print("YOU WON!")
    print("The word was:", word)
else:
    print("GAME OVER!")
    print("The word was:", word)




