from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass


class Subject(ABC):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass


class NewsPublisher(Subject):
    def __init__(self):
        self._observers = []
        self._latest_news = None

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self._latest_news)

    def add_news(self, news: str):
        self._latest_news = news
        self.notify()


class NewsSubscriber(Observer):
    def __init__(self, name: str):
        self.name = name

    def update(self, message: str):
        print(f"{self.name} received news: {message}")


class MobileAppSubscriber(Observer):
    def update(self, message: str):
        print(f"Mobile app notification: {message}")


if __name__ == "__main__":
    news_publisher = NewsPublisher()

    subscriber1 = NewsSubscriber("Alice")
    subscriber2 = NewsSubscriber("Bob")
    mobile_app_subscriber = MobileAppSubscriber()

    news_publisher.attach(subscriber1)
    news_publisher.attach(subscriber2)
    news_publisher.attach(mobile_app_subscriber)

    # news_publisher.add_news("New Python version released!")
