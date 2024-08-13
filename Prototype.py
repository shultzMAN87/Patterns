import copy


class Address:
    def __init__(self, country, sity, street):
        self.country = country
        self.sity = sity
        self.street = street

    def __str__(self):
        return f'{self.country}, {self.sity}, {self.street}'

class Person:
    def __init__(self, name, address: Address):
        self.name = name
        self.address = address

    # def __copy__(self):
    #     return copy.deepcopy(self)

    def __str__(self):
        return f'Я {self.name} мой адрес: {self.address}'


if __name__ == '__main__':
    pers1 = Person('Костя', Address('РФ', 'Владивосток', 'Нерчинская'))
    print(pers1)

    pers2 = copy.copy(pers1)
    print()
    pers2.name = 'Вася'
    pers2.address.street = 'Светланская'
    print(pers1)
    print(pers2)
