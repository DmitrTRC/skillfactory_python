import math
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class Figures(metaclass=ABCMeta):
    x: float = 0
    y: float = 0

    @property
    @abstractmethod
    def square(self):
        pass


@dataclass
class Circle(Figures):
    radius: float = 0

    @property
    def square(self):
        return math.pi * (self.radius ** 2)


@dataclass
class Rectangle(Figures):
    width: float = 0
    height: float = 0

    @property
    def square(self):
        return self.width * self.height

    def __str__(self):
        return f'Rectangle({self.x}, {self.y}, {self.width}, {self.height})'
