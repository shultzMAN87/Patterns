import threading


class Singleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self, value=None):
        if not hasattr(self, 'initialized'):
            self.value = value
            self.initialized = True


if __name__ == '__main__':
    first = Singleton()
    print(first)
    second = Singleton()
    print(second)
    print(first is second)