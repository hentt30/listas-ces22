from __future__ import annotations
from abc import ABC, abstractmethod


class Document:
    _state = None

    def __init__(self, state):
        self.transition_to(state)

    def transition_to(self, state):
        self._state = state
        self._state.document = self

    def user_publish(self):
        self._state.handle_publish_by_user()


class IState(ABC):
    @document.setter
    def document(self, document):
        self._document = document

    @abstractmethod
    def handle_publish_admin(self):
        """Documento é publicado pelo admin"""
    @abstractmethod
    def handle_publish_expired(self):
        """ Publicação expirada"""
    @abstractmethod
    def handle_publish_by_user(self):
        """Documento publicado pelo usuário"""
    @abstractmethod
    def handle_review_failed(self):
        """Documento rejeitado na revisão """
    @abstractmethod
    def handle_approved_admin(self):
        """ Documento aprovado pelo admin"""


class DraftState(State):
    pass


class PublishedState(State):
    pass


class ModerationState(State):
    pass