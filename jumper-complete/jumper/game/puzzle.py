import random

class Puzzle:
    """The player looking for the letters . 
    
    The responsibility of a Puzzle is to keep track of the letters of the word.
    
    Attributes:
        guess_word (char): The word to guess.
        word_letters (List[char]): The list of letters of the word.
        word_list (List[char]): The list of words to select
    """

    def __init__(self):
        """Constructs a new Puzzle.

        Args:
            self (Puzzle): An instance of Puzzle.
        """
        self._location = random.randint(0, 9)
        self.word_list = ['world', 'cars', 'window', 'door', 'cats', 'dogs', 'house', 'tower', 'court', 'palace']
        self.word = ''
        self.word_letters = []
    def get_word(self):
        """ Gets the word from list"""
        self.word = self.word_list[self._location]
        return self.word
        
    def get_letters(self, word):
        """Gets the letters of the word.
                Returns:
            list: The list of letters,
        """
        i = 0
        while i < len(word):
            self.word_letters.append(word[i:i+1]) 
            i += 1
        return self.word_letters
