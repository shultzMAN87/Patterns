from typing import  List
from typing import Dict


class Shared:
    def __init__(self, company: str, position: str):
        self.__company = company
        self.__position = position

    @property
    def company(self):
        return self.__company

    @property
    def position(self):
        return self.__position


class Unique:
    def __init__(self, name: str, passport: str):
        self.__name = name
        self.__passport = passport

    @property
    def name(self):
        return self.__name

    @property
    def passport(self):
        return self.__passport


class Flyweight:
    def __init__(self, shared: Shared):
        self.__shared = shared

    def process(self, unique: Unique):
        print('Новые данные: {}_{}'.format(self.__shared.company, self.__shared.position),
              'уникальные: {}_{}'.format(unique.name, unique.passport))

    def get_data(self) -> str:
        return self.__shared.company + '_' + self.__shared.position


class FlyweightFactory:
    def get_key(self, shared: Shared):
        return '{}_{}'.format(shared.company, shared.position)

    def __init__(self, shareds: List[Shared]):
        self.__flyweights: Dict[str, Flyweight] = {}
        for shared in shareds:
            self.__flyweights[self.get_key(shared)] = Flyweight(shared)

    def get_flyweights(self, shared: Shared):
        key: str = self.get_key(shared)

        if self.__flyweights.get(key) is None:
            print('Af,hbrf')
            self.__flyweights[key] = Flyweight(shared)
        else:
            print('dcdcdc')
        return self.__flyweights[key]

    def list_flyweight(self):
        count: int = len(self.__flyweights)
        print('Фабрика легковесов {}:'.format(count))
        for pair in self.__flyweights.values():
            print(pair.get_data())


def add_spec_database(ff: FlyweightFactory,
                      company: str,
                      position: str,
                      name: str,
                      passport: str):

    print()
    flyweight = ff.get_flyweight(Shared(company, position))
    flyweight.process(Unique(name, passport))


if __name__ == '__name__':

    shared_list: List[Shared] = (Shared('asa', 'sas'), Shared('asa', 'sas'))

    factory = FlyweightFactory(shared_list)
    factory.list_flyweights()

    add_spec_database(factory,
                      'asd',
                      'asd',
                      'asd',
                      'asd')

    factory.list_flyweights()