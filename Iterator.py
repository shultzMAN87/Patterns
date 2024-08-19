from typing import List, Any, Iterator

# Итератор
class NameIterator(Iterator):
    def __init__(self, names: List[str]):
        self._names = names
        self._index = 0

    def __next__(self) -> str:
        if self._index < len(self._names):
            result = self._names[self._index]
            self._index += 1
            return result
        else:
            raise StopIteration

    def __iter__(self) -> 'NameIterator':
        return self

# Агрегат (Коллекция)
class NameCollection:
    def __init__(self):
        self._names: List[str] = []

    def add_name(self, name: str):
        self._names.append(name)

    def __iter__(self) -> NameIterator:
        return NameIterator(self._names)

# Пример использования
if __name__ == "__main__":
    collection = NameCollection()
    collection.add_name("Alice")
    collection.add_name("Bob")
    collection.add_name("Charlie")

    for name in collection:
        print(name)