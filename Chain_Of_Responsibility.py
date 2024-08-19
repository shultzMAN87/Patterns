from abc import ABC, abstractmethod


class Handler(ABC):
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request: str):
        pass


class SupportHandler(Handler):
    def handle(self, request: str):
        if request == "Technical Issue":
            print("Support: Handling technical issue.")
        elif self.next_handler:
            self.next_handler.handle(request)


class SalesHandler(Handler):
    def handle(self, request: str):
        if request == "Sales Inquiry":
            print("Sales: Handling sales inquiry.")
        elif self.next_handler:
            self.next_handler.handle(request)


class BillingHandler(Handler):
    def handle(self, request: str):
        if request == "Billing Issue":
            print("Billing: Handling billing issue.")
        elif self.next_handler:
            self.next_handler.handle(request)


if __name__ == "__main__":
    support = SupportHandler()
    sales = SalesHandler()
    billing = BillingHandler()

    support.set_next(sales).set_next(billing)

    # Запросы
    support.handle("Sales Inquiry")
    support.handle("Billing Issue")
    support.handle("Technical Issue")
    support.handle("Unknown Request")
