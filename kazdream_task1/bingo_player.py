from random import randint
from copy import deepcopy
from typing import List

from utils import Observer


class BingoPlayer(Observer):
    """
    Игрок в Бинго. У игрока есть имя и билетик с 5 случайными числами( числа от 1 до 99). Для
    создания новых игроков используется паттерн Прототип.
    """

    def __init__(self) -> None:
        """
        Конструктор класса. При инициализации прототипа объявляются закрытые атрибуты класса,
        с присвоением им значений None.
        """
        self._name: str = None
        self._ticket: List[int] = None

    @property
    def name(self) -> str:
        """
        Getter для доступа к атрибуту name.

        Returns:
            str: имя игрока
        """
        return self._name

    @property
    def ticket(self) -> List[int]:
        """
        Getter для доступа к атрибуту ticket.

        Returns:
            List[int]: билетик игрока
        """
        return self._ticket

    def initialize(self, name: str) -> None:
        """
        Инициализирует прототип перед его клонированием.

        Args:
            name (str): имя игрока
        """
        # Присвоить игроку имя
        self._name = name
        # Сформировать билетик с пятью случайными числами в диапазоне от 1 до 99
        self._ticket = [randint(1, 99) for _ in range(5)]

    def clone(self) -> 'BingoPlayer':
        """
        Клонирует прототип игрока. Перед вызовом метода обязательно необходимо инициализировать
        прототип.

        Returns:
            BingoPlayer: игрок в бинго
        """
        return deepcopy(self)


if __name__ == '__main__':
    player_prototype = BingoPlayer()

    for a_name in ['Valentin', 'Egor']:
        player_prototype.initialize(a_name)
        a_player = player_prototype.clone()
        print(f"Player: {a_player.name} has ticket {a_player.ticket}")
