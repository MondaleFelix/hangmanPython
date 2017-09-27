import random

guesses = 6
printedWord = []

# This function returns a random word
def loadWord():
   f = open('hangman_words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = list(random.choice(wordsList))
   return secretWord

# This function inserts the users input and returns results
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

# This function validates winning or losing
def isWordGuessed(secretWord, printedWord):
    if secretWord == printedWord:
      print(printedWord)
      print("Winner")
    elif guesses == 0:
      print("Fucking loser")


# This function prints the underlines for the user
def getGuessedWord(secretWord):
    for i in secretWord:
      printedWord.append("_")
    guessLetter()



def getAvailableLetters(lettersGuessed):
    pass

def hangman(secretWord):
    pass


secretWord = loadWord()
getGuessedWord(secretWord)
hangman(loadWord())
