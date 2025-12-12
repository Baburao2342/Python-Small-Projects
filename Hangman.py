import HangmanWords as hw
import random

print('''

    Welcome to the hangman game! Choose your difficulty and guess the word.
    Good Luck!
      
''')

difficulty = input("Enter the difficulty (easy/medium/hard): ")

def easy():
    word = hw.easy[random.randint(0, 9)]
    palette = ['-', '-', '-', '-']
    return word, palette
def medium():
    word = hw.medium[random.randint(0,9)]
    palette = ['-', '-', '-', '-', '-', '-']
    return word, palette
def hard():
    word = hw.hard[random.randint(0, 9)]
    palette = ['-', '-', '-', '-', '-', '-', '-', '-']
    return word, palette

diff_dict = {
    'easy': easy(),
    'medium': medium(),
    'hard': hard()
}

if difficulty in diff_dict:
    word, palette = diff_dict[difficulty]


count = 1
victory = False


while count != 10:
    print(f'\nAttempt {count}!\n')

    print(hw.hangman[count])
    
    for i in palette:
        print(i, end='')
    guess = input('\nEnter your guess: ')

    if word.count(guess) == 1:
        palette[word.index(guess)] = guess
    elif word.count(guess) > 1:
        index = []
        for i in word:
            if i == guess:
                index.append(word.index(i))
        for j in index:
            palette[j] = guess
    else:
        print('\nWrong!')

    if '-' not in palette:
        victory = True
        break

    count += 1

if victory:
    print(f'\nYou guessed in {count} tries!')
else:
    print("\nLol couldn't guess")
    print(f"The word was: {word}")
