import random

class Hilo:
    """A generation of a car 1 to 13.

       The responsibility of Hilo is to keep track of the card selected 
   
        Attributes:
        value (int): The number of spots on the side facing up.
    """

    def __init__(self):
        """Constructs a new instance of Die.

        Args:
            self (Die): An instance of Die.
        """
        self.value = 0

    def guess_card(self):
        """Selects a new random card.
        
        Args:
            self (Hilo): An instance of Hilo.
        """
        self.value = random.randint(1, 13)