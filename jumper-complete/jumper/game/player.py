import random

class Player:
    """The person managing the parachute. 
    
    The responsibility of Parachute is to keep track of the parachute based on the player input. 
    
    Attributes:
        _lines of parachute (List): The lines of the parachute (eight).
        _remaining lines of parachute (List): The remaining lines of the parachute 
    """

    def __init__(self):
        """Constructs a new parachute.

        Args:
            self (Parachute): An instance of Parachute.
        """
        self.lines = ['\ ', '/', '___',  ]
    
    def get_hint(self):
        """Gets a hint for the seeker.

        Args:
            self (Hider): An instance of Hider.
        
        Returns:
            string: A hint for the seeker.
        """
        hint = "(-.-) Nap time."
        if self._distance[-1] == 0:
            hint = "(;.;) You found me!"
        elif self._distance[-1] > self._distance[-2]:
            hint = "(^.^) Getting colder!"
        elif self._distance[-1] < self._distance[-2]:
            hint = "(>.<) Getting warmer!"
        return hint

    def is_found(self):
        """Whether or not the hider has been found.

        Args:
            self (Hider): An instance of Hider.
            
        Returns:
            boolean: True if the hider was found; false if otherwise.
        """
        return (self._distance[-1] == 0)
        
    def watch_seeker(self, seeker):
        """Watches the seeker by keeping track of how far away it is.

        Args:
            self (Hider): An instance of Hider.
        """
        distance = abs(self._location - seeker.get_location())
        self._distance.append(distance)