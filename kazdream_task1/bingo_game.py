"""
Module contains BingoGame class.
"""
from typing import List
from random import choice

from utils import Observer, Subject
from bingo_player import BingoPlayer


RANGE_BEGIN: int = 1
RANGE_END: int = 100


class BingoGame(Subject):
    """
    Bingo game. Each player has a ticket with 5 random numbers (numbers from 1 to 99).
    The game randomly chooses a number between 1 and 99 and notifies the players about
    this number. The player who first collected his combination must call out his name
    and the game will stop.
    """

    def __init__(self, player_prototype: BingoPlayer) -> None:
        """
        Class constructor.

        Args:
            player_prototype (BingoPlayer): player prototype, used to create players
        """
        self._player_prototype = player_prototype
        self._observers: List[Observer] = []
        self._number = 0
        self._game_state = True

    @property
    def number(self) -> int:
        """
        Getter for the number attribute.

        Returns:
            int: value of number attribute
        """
        return self._number

    @property
    def game_state(self) -> bool:
        """
        Getter for the game state attribute.

        Returns:
            bool: current game state
        """
        return self._game_state

    @game_state.setter
    def game_state(self, a_state: bool) -> None:
        """
        Setter for the game state attribute.

        Args:
            a_state (bool): current game state
        """
        self._game_state = a_state

    # Observer pattern methods
    def attach(self, observer: 'Observer') -> None:
        self._observers.append(observer)

    def detach(self, observer: 'Observer') -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def initialize_players(self, player_names: List[str]) -> None:
        """
        Initializes Bingo players.

        Args:
            player_names (List[str]): list of player names
        """
        for player_name in player_names:
            # Initialize prototype
            self._player_prototype.initialize(player_name)
            # Clone player prototype
            a_player: BingoPlayer = self._player_prototype.clone()
            # Subscribe player for updates
            self.attach(a_player)

    def start_game(self) -> None:
        """
        Starts the Bingo game.
        """
        # Initilize Bingo game sample of the numbers
        numbers_in_the_game: List[int] = list(range(RANGE_BEGIN, RANGE_END))
        # Print welcome message
        print('Welcome to the Bingo game!')
        # While winner is not determinated
        while self._game_state:
            # Pick a random number from the sample
            self._number = choice(numbers_in_the_game)
            # Remove the number from the sample
            numbers_in_the_game.remove(self._number)
            # Notify players about the number
            print(f'We got number: {self._number}')
            self.notify()


if __name__ == '__main__':
    philosopher_names: List[str] = [
        'Thomas Aquinas',
        'Aristotle',
        'Confucius',
        'René Descartes',
        'Ralph Waldo Emerson'
    ]

    a_game = BingoGame(BingoPlayer())
    a_game.initialize_players(philosopher_names)
    a_game.start_game()
