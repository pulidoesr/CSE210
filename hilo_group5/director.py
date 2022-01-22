from hilo import Hilo

class Director:
      """A person who directs the game. 
    
        The responsibility of a Director is to control the sequence of play.

        Attributes:
        hilo (List[Hilo]): A list of Hilo instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
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
        self.get_card()
        self.show_card()
        while self.is_playing:
            self.get_guess()
            self.get_card()
            self.show_card()
            self.eval_card()
            self.do_updates()
            self.do_outputs()
            self.get_input()
            self.get_card()
            self.show_card()
      def get_card(self):
        """ Get the card first and keep the previous value """
        if not self.is_playing:
          return
        self.previous_card = self.guess_card
        hilo = Hilo() 
        hilo.guess_card()
        self.guess_card = hilo.value
      def show_card(self):
        """ Show the new card selected """
        if not self.is_playing:
          return
        print(f'The card is: {self.guess_card}')
      def get_guess(self):
        """Ask the user if the next card is Higher or Lower.
        """    
        self.guess_hl = input('Higer or Lower (h/l): ')
      def eval_card(self):
        """ Verify if the next guess was right or not """
        if self.guess_hl == 'h':
          if self.guess_card > self.previous_card:
            self.score = 100
          else:
            self.score = -75
            self.is_guess = False
        if self.guess_hl == 'l':
          if self.guess_card < self.previous_card:
            self.score = 100
          else:
            self.score = -75
            self.is_guess = False
        if self.first:
          self.score += 300
          self.first = False
      def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
           return  
        self.total_score += self.score
      def do_outputs(self):
        """Displays the score. 
           Args:
           self (Director): An instance of Director.
        """
        if not self.is_playing:
            return
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
      def get_input(self):
        """ Continue Playing """
        self.play_again = input('Play again (y/n): ')
        
        self.is_playing = (self.play_again == 'y')