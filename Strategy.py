from abc import ABC, abstractmethod
from typing import List

# Интерфейс стратегии
class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: List[int]) -> List[int]:
        pass

# Конкретная стратегия - сортировка пузырьком
class BubbleSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        n = len(data)
        for i in range(n):
            for j in range(0, n-i-1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]
        return data

# Конкретная стратегия - быстрая сортировка
class QuickSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        if len(data) <= 1:
            return data
        pivot = data[len(data) // 2]
        left = [x for x in data if x < pivot]
        middle = [x for x in data if x == pivot]
        right = [x for x in data if x > pivot]
        return self.sort(left) + middle + self.sort(right)

# Конкретная стратегия - сортировка вставками
class InsertionSortStrategy(SortingStrategy):
    def sort(self, data: List[int]) -> List[int]:
        for i in range(1, len(data)):
            key = data[i]
            j = i - 1
            while j >= 0 and key < data[j]:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = key
        return data

# Контекст, который использует стратегию
class Sorter:
    def __init__(self, strategy: SortingStrategy):
        self._strategy = strategy

    def set_strategy(self, strategy: SortingStrategy):
        self._strategy = strategy

    def sort(self, data: List[int]) -> List[int]:
        return self._strategy.sort(data)

# Пример использования
if __name__ == "__main__":
    data = [5, 2, 9, 1, 5, 6]

    sorter = Sorter(BubbleSortStrategy())
    print("Bubble Sort:", sorter.sort(data.copy()))

    sorter.set_strategy(QuickSortStrategy())
    print("Quick Sort:", sorter.sort(data.copy()))

    sorter.set_strategy(InsertionSortStrategy())
    print("Insertion Sort:", sorter.sort(data.copy()))