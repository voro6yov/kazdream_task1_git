from abc import ABC, abstractmethod

__all__ = ['Subject', 'Observer']


class Subject(ABC):
    """
    Интерфейс субъекта, содержит объявления методов для управления подписчиками.
    """
    @abstractmethod
    def attach(self, observer: 'Observer') -> None:
        """
        Подписывает наблюдателя на обновления субъекта.

        Args:
            observer (Observer): наблюдатель, которого необходимо подписать на обнавления субъекта
        """

    @abstractmethod
    def detach(self, observer: 'Observer') -> None:
        """
        Отписывает наблюдателя от обновлений субъекта.

        Args:
            observer (Observer): наблюдатель, которого необходимо отписать от обнавлений субъекта
        """

    @abstractmethod
    def notify(self) -> None:
        """
        Уведомляет наблюдателей о произошедшем событии.
        """


class Observer(ABC):
    """
    Интерфейс наблюдателя, содержит метод, который используется субъектом для
    обнавления состояния наблюдателя.
    """
    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Сообщает наблюдателю об изменении состояния субъекта.

        Args:
            subject (Subject): наблюдаемый субъект
        """
