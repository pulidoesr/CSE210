from game.player import Player
from game.puzzle import Puzzle


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        Puzzle: The game's guess word.
        is_playing (boolean): Whether or not to keep playing.
        player (Player): The player that guess the letter.
        terminal_service: For getting and displaying information on the terminal.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self._puzzle = Puzzle()
        self._player = Player()
        self._is_playing = True
        self._word = ''
        self._guess_letter = ''
        
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        self._word = self._puzzle.get_puzzle()
        self._player.print_parachute()
        self._puzzle.blank_line()
        while self._is_playing:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """Look for the random word.
           Ask for the guess letter

        Args:
            self (Director): An instance of Director.
        """
        
        self._guess_letter = input('Guess a letter [a-z]: ')
         
    def _do_updates(self):
        """Check the guess letter
           Update the parachute
           Find if the player can continue the game 8 errors or word guessed
        Args:
            self (Director): An instance of Director.
        """
        self.is_found = self._puzzle.check_guess(self._guess_letter)
        self._puzzle.show_word()
        if self.is_found: 
           self._is_playing = self._puzzle.is_solved()
        else:
           self._is_playing = self._player.update_parachute(self.is_found)
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """
        self._player.print_parachute()
        