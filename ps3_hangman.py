import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    
    We'll test this by seeing if the letter is in the secretWord. 
    If it is, we'll count how many times it appears adding to the total length.
    If this length matches the length of the secretWord, then the word is guessed.
    '''
    length = 0 
    for ltr in lettersGuessed:
        if ltr in secretWord:
            length += secretWord.count(ltr)
    return len(secretWord) == length



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    guessedWord = []
    for idx, ltr in enumerate(secretWord):
        if ltr in lettersGuessed:
            guessedWord.append(ltr)
        else:
            guessedWord.append('_')
    return " ".join(guessedWord)



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    availableLetters = []
    for ltr in string.ascii_lowercase:
        if not ltr in lettersGuessed:
            availableLetters.append(ltr)
    return ", ".join(availableLetters)


    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    #Welcome message
    print("Welcome to Hangman!\nThe word I am thinking of is " + str(len(secretWord)) + " letters long")
    
    numGuesses = int(8)
    lettersGuessed = []
    while numGuesses > 0:
        print("****************************************")
        print("You have " + str(numGuesses) + " guesses left!") #Display number of guesses
        print("Available letters: " + getAvailableLetters(lettersGuessed)) #Print letters to choose from
        
        #Input letter
        ltr = input("Please guess a letter: ")
        ltr = ltr.lower()
        
        #Check for valid input
        while ltr in lettersGuessed or not ltr.isalpha() or len(ltr) != 1:
            ltr = input("Invalid input! Please enter an available letter: ")
            ltr = ltr.lower()
        lettersGuessed.append(ltr)
        
        #Check to see if the letter is in the secretWord
        if ltr in secretWord:
            print("Good guess: " + getGuessedWord(secretWord, lettersGuessed))
        else:
            print("Oops! That letter is not in my word: " + getGuessedWord(secretWord, lettersGuessed))
            numGuesses -= 1 #decrease number of guesses by 1 if wrong
        
        #Check to see if word has been guessed
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print("****************************************")
            print("Congrats! You win! The secret word was " + secretWord)
            return

    #Lost game
    print("****************************************")
    print("Sorry, you ran out of guesses. The word was " + secretWord)
    return





# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
