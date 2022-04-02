from abc import ABC, abstractmethod

class User(ABC):

    def __init__(self, name):
        self.name = name



