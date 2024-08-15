import abc


class Item(metaclass=abc.ABCMeta):
    def __init__(self, name: str):
        self._item_name: str = name
        self._owner_name: str = None

    def set_owner(self, o: str):
        self._owner_name = o

    @abc.abstractmethod
    def add(self, sub_item: 'Item'):
        pass

    @abc.abstractmethod
    def display(self):
        pass


class ClickableItem(Item):
    def __init__(self, name: str):
        super().__init__(name)

    def add(self, sub_item: Item):
        raise Exception('Кликабельному элементу нельзя добавить подэлемент')

    def display(self):
        print(self._owner_name + self._item_name)


class DropDownItem(Item):
    def __init__(self, name: str):
        super().__init__(name)
        self._children = []

    def add(self, sub_item: Item):
        sub_item.set_owner(self._item_name)
        self._children.append(sub_item)

    def display(self):
        for item in self._children:
            if self._owner_name is not None:
                print(self._owner_name, end='')
            item.display()


if __name__ == '__main__':
    file: Item = DropDownItem('Файл->')

    create: Item = DropDownItem('Создать->')
    open_: Item = DropDownItem('Открыть->')
    exit_: Item = ClickableItem('Выход')

    file.add(create)
    file.add(open_)
    file.add(exit_)

    project: Item = ClickableItem('Проект')
    repository: Item = ClickableItem('Репозиторий')

    create.add(project)
    open_.add(repository)

    file.display()