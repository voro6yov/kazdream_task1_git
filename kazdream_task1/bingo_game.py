from typing import List
from random import choice

from utils import Observer, Subject
from bingo_player import BingoPlayer


class BingoGame(Subject):
    """
    Игра в Бинго. У каждого игрока есть билетик с 5 случайными числами(числа от 1 до 99). 
    Игра случайно выбирает число от 1 до 99 и оповещает игроков об этом числе. Игрок, который 
    первым собрал свою комбинацию, должен выкрикнуть свое имя и игра остановится.
    """
    def __init__(self, player_prototype: BingoPlayer) -> None:
        self._player_prototype = player_prototype
        self._observers: List[Observer] = []
        self._number = 0
        self._game_state = True

    @property
    def number(self) -> int:
        return self._number

    @property
    def game_state(self) -> bool:
        return self._game_state

    @game_state.setter
    def game_state(self, a_state: bool) -> None:
        self._game_state = a_state

    def attach(self, observer: 'Observer') -> None:
        self._observers.append(observer)

    def detach(self, observer: 'Observer') -> None:
        self._observers.remove(observer)

    def notify(self) -> None:
        for observer in self._observers:
            observer.update(self)

    def initialize_players(self, player_names: List[str]) -> None:
        for player_name in player_names:
            self._player_prototype.initialize(player_name)
            a_player: BingoPlayer = self._player_prototype.clone()
            self.attach(a_player)

    def start_game(self) -> None:
        numbers_in_the_game: List[int] = list(range(1, 100))
        print('Welcome to the Bingo game!')
        while self._game_state:
            self._number = choice(numbers_in_the_game)
            numbers_in_the_game.remove(self._number)
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