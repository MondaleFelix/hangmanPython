import random

guesses = 6
solution = []
lettersGuessed = []
def loadWord():
   f = open('hangman_words.txt', 'r')
   wordsList = f.readlines()
   f.close()

   wordsList = wordsList[0].split(' ')
   secretWord = list(random.choice(wordsList))
   return secretWord

def getGuessedWord(secretWord, printedWord):
      for i in secretWord:
        printedWord.append("_")
      print(printedWord)

# def guessLetter(secretWord, printedWord):
#       global guesses
#       letter = raw_input("Enter a letter: ")
#       if letter in secretWord:
#         printedWord.append(letter)
#       else:
#         print("false")
#       print(printedWord)
#       getGuessedWord(secretWord, printedWord)
#       guessLetter(secretWord, printedWord)

  # print("false")
  # guesses = guesses - 1
  #     print(guesses)

  # if letter in secretWord:
  #   global solution
  #   solution.append(letter)
  #   if letter in solution:
  #   print(True)
  #   print(solution)
  # else:
  #   print(False)




printedWord = []
loadWord()
guessLetter(loadWord(), printedWord)






# def isWordGuessed(secretWord, lettersGuessed):
#     '''
#     secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
#     lettersGuessed: list of letters that have been guessed so far.
#     returns: boolean, True only if all the letters of secretWord are in lettersGuessed;
#       False otherwise
#     '''
#     # FILL IN YOUR CODE HERE...





'''
secretWord: string, the random word the user is trying to guess.  This is selected on line 9.
lettersGuessed: list of letters that have been guessed so far.
returns: string, of letters and underscores.  For letters in the word that the user has
guessed correctly, the string should contain the letter at the correct position.  For letters
in the word that the user has not yet guessed, shown an _ (underscore) instead.
'''
# FILL IN YOUR CODE HERE...




# def getAvailableLetters(lettersGuessed):
#     '''
#     lettersGuessed: list of letters that have been guessed so far
#     returns: string, comprised of letters that represents what letters have not
#       yet been guessed.
#     '''



# def hangman(secretWord):
#   guessLetter()

# '''
#     secretWord: string, the secret word to guess.

#     Starts up a game of Hangman in the command line.

#     * At the start of the game, let the user know how many
#       letters the secretWord contains.

#     * Ask the user to guess one letter per round.

#     * The user should receive feedback immediately after each guess
#       about whether their guess appears in the computer's word.

#     * After each round, you should also display to the user the
#       partially guessed word so far, as well as letters that the
#       user has not yet guessed.
#     '''
#     # FILL IN YOUR CODE HERE...




# secretWord = loadWord()
# hangman(secretWord)

