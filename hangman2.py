import random

guesses = 6
printedWord = []

def loadWord():
   f = open('hangman_words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = list(random.choice(wordsList))
   return secretWord

def guessLetter():
    global guesses
    while guesses > 0 and secretWord != printedWord:
      print(printedWord)
      letter = raw_input("Enter a letter: ")
      if letter in secretWord:
        for i in range(len(secretWord)):
          if letter == secretWord[i]:
            printedWord[i] = letter
      else:
        guesses = guesses - 1
        print("False, you have " + str(guesses) + " left")
      isWordGuessed(secretWord, printedWord)
      guessLetter()

def isWordGuessed(secretWord, printedWord):
    if secretWord == printedWord:
      print(printedWord)
      print("Winner")
    elif guesses == 0:
      print("Fucking loser")


def getGuessedWord(secretWord):
    for i in secretWord:
      printedWord.append("_")
    guessLetter()



def getAvailableLetters(lettersGuessed):



def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up a game of Hangman in the command line.

    * At the start of the game, let the user know how many
      letters the secretWord contains.

    * Ask the user to guess one letter per round.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each round, you should also display to the user the
      partially guessed word so far, as well as letters that the
      user has not yet guessed.
    '''
    # FILL IN YOUR CODE HERE...

secretWord = loadWord()
getGuessedWord(secretWord)
hangman(loadWord())
