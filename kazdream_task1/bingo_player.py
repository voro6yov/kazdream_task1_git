"""
Module contains BingoPlayer class.

Developed by Valentin Vorobyov.
"""
from random import sample
from copy import deepcopy
from typing import List

from utils import Observer, Subject


RANGE_BEGIN: int = 1
RANGE_END: int = 100
DIGITS_NUMBER: int = 5


class BingoPlayer(Observer):
    """
    Bingo player. The player has a name and a ticket with 5 random numbers (numbers from 1 to 99).
    The Prototype pattern is used to create new players. The Observer pattern is used to notify
    player about current Bingo number.
    """

    def __init__(self) -> None:
        """
        Class constructor.
        """
        # Initialize private attributes
        self._name: str = None
        self._ticket: List[int] = None

    @property
    def name(self) -> str:
        """
        Getter of the name attribute.

        Returns:
            str: player name
        """
        return self._name

    @property
    def ticket(self) -> List[int]:
        """
        Getter of the ticket attribute.

        Returns:
            List[int]: player's ticket
        """
        return self._ticket

    def initialize(self, name: str) -> None:
        """
        Initializes the prototype before cloning it.

        Args:
            name (str): player name
        """
        # Assign player name
        self._name = name
        # Generate a ticket with five random numbers ranging from 1 to 99
        self._ticket = sample(range(RANGE_BEGIN, RANGE_END), DIGITS_NUMBER)

    def clone(self) -> 'BingoPlayer':
        """
        Clones a prototype player. The prototype must be initialized before calling the method.

        Returns:
            BingoPlayer: a bingo player
        """
        return deepcopy(self)

    def update(self, subject: Subject) -> None:
        """
        Updates player's information about current Bingo number.

        Args:
            subject (Subject): Bingo game
        """
        # Get current Bingo number
        current_number = subject.number
        # If current Bingo number in ticket
        if current_number in self._ticket:
            # Remove it from ticket
            self._ticket.remove(current_number)
            # If ticket doesn't has numbers
            if self._ticket == []:
                # Print winner message
                print(f'{self._name.upper()} BINGO!!!')
                # Finish the Bingo game
                subject.game_state = False
