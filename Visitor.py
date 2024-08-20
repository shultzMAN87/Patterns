from abc import ABC, abstractmethod

class Visitor(ABC):
    @abstractmethod
    def visit_pdf(self, element):
        pass

    @abstractmethod
    def visit_word(self, element):
        pass


class ExportVisitor(Visitor):
    def visit_pdf(self, element):
        print(f"Exporting PDF document: {element.content}")

    def visit_word(self, element):
        print(f"Exporting Word document: {element.content}")

class PrintVisitor(Visitor):
    def visit_pdf(self, element):
        print(f"Printing PDF document: {element.content}")

    def visit_word(self, element):
        print(f"Printing Word document: {element.content}")


class DocumentElement(ABC):
    @abstractmethod
    def accept(self, visitor: Visitor):
        pass


class PDFDocument(DocumentElement):
    def __init__(self, content: str):
        self.content = content

    def accept(self, visitor: Visitor):
        visitor.visit_pdf(self)

class WordDocument(DocumentElement):
    def __init__(self, content: str):
        self.content = content

    def accept(self, visitor: Visitor):
        visitor.visit_word(self)


if __name__ == "__main__":
    documents = [
        PDFDocument("PDF Content 1"),
        WordDocument("Word Content 1"),
        PDFDocument("PDF Content 2"),
        WordDocument("Word Content 2"),
    ]

    export_visitor = ExportVisitor()
    print_visitor = PrintVisitor()

    for doc in documents:
        doc.accept(export_visitor)
        doc.accept(print_visitor)
