from game.player import Player
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        hider (Hider): The game's hider.
        is_playing (boolean): Whether or not to keep playing.
        seeker (Seeker): The game's seeker.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._parachute = Player()
        self._is_playing = True
        self._word = ''
        self._guess_letter = ''
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Look for the random word.
           Paint the parachute
           Ask for the letter

        Args:
            self (Director): An instance of Director.
        """
        self._word = self._puzzle.get_puzzle()
        print(f'{self._word}')
        """ Paint the parachute """
        self._guess_letter = input('Guess a letter [a-z]: ')
        self.is_found = self._puzzle.check_guess(self._guess_letter)
        if self.is_found:
           self._is_playing = self._puzzle.show_word() 
           
        
    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        