"""
Module contains abstract classes of Observer pattern.

Developed by Valentin Vorobyov.
"""

from abc import ABC, abstractmethod

__all__ = ['Subject', 'Observer']


class Subject(ABC):
    """
    The subject interface contains method declarations for managing subscribers.
    """
    @abstractmethod
    def attach(self, observer: 'Observer') -> None:
        """
        Subscribes the observer to updates to the subject.

        Args:
            observer (Observer): observer subscribed to subject updates
        """

    @abstractmethod
    def detach(self, observer: 'Observer') -> None:
        """
        Unsubscribes the observer from updates to the subject.

        Args:
            observer (Observer): observer unsubscribed from subject updates
        """

    @abstractmethod
    def notify(self) -> None:
        """
        Notifies observers of an event that has occurred.
        """


class Observer(ABC):
    """
    The observer interface contains a method that the subject uses to
    update the observer state.
    """
    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Updates current state.

        Args:
            subject (Subject): observed subject
        """
