import random
from game.terminal_service import TerminalService

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
        """             0    1    2   3     4    5      6   7   8   9   10  11  12  13""" 
        self._lines = ['\ ','\ ','/','___','\ ','───', '/','/','☺','/','|','\ ','/','\ ']
        self._errors = 0
        self._terminal_service = TerminalService()
    
    def print_parachute(self):
        """Print parachute. """
        tline = " " + self._lines[3]
        self._terminal_service.write_text(tline)
        tline = self._lines[2] + "   " + self._lines[4]
        self._terminal_service.write_text(tline)
        tline = " " + self._lines[5]
        self._terminal_service.write_text(tline)
        tline = self._lines[1] + "  " + self._lines[6]
        self._terminal_service.write_text(tline)
        tline = " " + self._lines[0] + self._lines[7]
        self._terminal_service.write_text(tline)
        tline = "  " + self._lines [8]
        self._terminal_service.write_text(tline)
        tline = " " + self._lines[9] + self._lines[10] + self._lines[11]
        self._terminal_service.write_text(tline)
        tline = " " + self._lines[12] + " " + self._lines[13]
        self._terminal_service.write_text(tline)
        return

    def update_parachute(self, found):
        """Update the Parachute based on letter guess or not.
           Args:
                found or not
           Returns:
        """
        is_playing = True
        if not(found):
           self._errors += 1
           if self._errors <= 8:
              self._lines[self._errors-1] = "  "
           if self._errors == 8:
               is_playing = False
        return is_playing
        