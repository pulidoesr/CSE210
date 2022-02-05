"""
The hider's location is a random number between 1 and 1000.
The seeker searches for the hider by guessing its location.
If the guess is closer to the hider's location it says, "Getting warmer!"
If the guess is farther away from the hider's location it says, "Getting colder!"
If the guess is correct the hider says, "You found me!". The game is over.
"""
from hider import Hider  
from os import system, name



class Director:
      """A person who directs the game. 
    
        The responsibility of a Director is to control the sequence of play.

        Attributes:
        hider (List[Hilo]): A list of Hider instances.
        is_playing (boolean): Whether or not the game is being played.
      """
      def __init__(self):
        """Constructs a new Director. 
          Args:
          self (Director): an instance of Director.
        """
        self.first = True
        self.guess_card = 0
        self.previous_card = 0
        self.guess_hl = ''
        self.play_again = ''
        self.is_guess = True
        self.is_playing = True
        self.score = 0
        self.total_score = 0

      def start_game(self):
        """ Starts the game by running the main game loop.
            Args:
            self (Director): an instance of Director
        """
        clear()
        self.get_hider()
        while self.is_playing:
            self.get_guess()
            self.eval_find()
            self.do_outputs()
            self.get_input()

      def get_hider(self):
        """ Get the hider first """
        if not self.is_playing:
          return
        hider = Hider() 
        hider.ramdom_hider()
        self.ramdom_hider = hider.value
      
      def get_guess(self):
        """Ask the user to enter the location.
        """    
        self.guess_location = input('Input the location: ')
      def eval_find(self):
        """ Verify if the guess is closer or not"""
        self.difference = self.ramdom_hider - self.guess_location
        if self.difference == 0:
          self.text = f'You found me!'
          self.is_playing = False
        else:
          if self.difference < 10:
            self.text = f'You are getting warmer!'
          else:
            self.text = f'You are getting colder!'
      
      def do_outputs(self):
        """Displays the score. 
           Args:
           self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        if self.is_guess:
           self.text = colored(0,2550,0, self.text)
        else:
           self.text = colored(255,0,0,self.text)
        print(f"{self.text}")
        self.is_guess = True
        self.is_playing == (self.score > 0)
      def get_input(self):
        """ Continue Playing """
        self.play_again = input('Play again (y/n): ')
        self.is_playing = (self.play_again == 'y')
        print(f' ')

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
        
def colored(r, g, b, text):
    return "\033[38;2;{};{};{}m{} \033[38;2;255;255;255m".format(r, g, b, text)