import math
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class Figures(metaclass=ABCMeta):

    @property
    @abstractmethod
    def square(self):
        pass


@dataclass
class Circle(Figures):
    radius: float

    @property
    def square(self):
        return math.pi * (self.radius ** 2)
