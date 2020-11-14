from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from enum import Enum


class ShelterStatus(Enum):
    OUT_OF_HOME = 'Has no permanent Home'
    WAITING = 'Has intend to take'
    HAS_HOME = 'Found home'
    UNKNOWN = 'Unknown'


class Gender(Enum):
    MALE = 'Male'
    FEMALE = 'Female'


@dataclass
class Animal(metaclass=ABCMeta):
    gender: Gender
    age: float
    status: ShelterStatus = ShelterStatus.UNKNOWN

    @property
    @abstractmethod
    def species(self):
        pass


@dataclass
class Cat(Animal):
    nickname: str = ''
    breed: str = ''
    registration_id: str = ''

    @property
    def species(self):
        return 'Cat'

    def __str__(self):
        return f'Species: {self.species} \nName: {self.nickname} \nGender: {self.gender.value} \nAge: {self.age} ' \
               f'\nStatus:' \
               f' {self.status.value} ' \
               f'\nBreed: ' \
               f'{self.breed} \nID: {self.registration_id}\n'
