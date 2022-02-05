import random

class Hider:
    """A generation of a hider 1 to 1000.

       The responsibility of hider is to keep track of the hider number 
   
        Attributes:
        value (int): The random number
    """

    def __init__(self):
        """Constructs a new instance of Hider.

        Args:
            self (Hider): An instance of Hider.
        """
        self.value = 0

    def random_hider(self):
        """Selects a new random hider.
        
        Args:
            self (Hider): An instance of Hider.
        """
        self.value = random.randint(1, 1000)