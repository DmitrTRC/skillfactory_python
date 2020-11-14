from typing import List

from demo_lib.cats import Cat, Gender, ShelterStatus

if __name__ == '__main__':
    cats: List[Cat] = list()

    cats.append(Cat(age=2, nickname='Baron', gender=Gender.MALE, status=ShelterStatus.OUT_OF_HOME))
    cats.append(Cat(age=2, nickname='Sam', gender=Gender.MALE, status=ShelterStatus.OUT_OF_HOME))

    for cat in cats:
        print(cat)
