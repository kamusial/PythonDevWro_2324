from PyQt6.QtGui import QTextDocument
from PyQt6.QtPrintSupport import QPrinter
from PyQt6.QtWidgets import QApplication
from markdown import markdown


def read_file(filepath: str) -> str:
    return open(filepath).read()


def prepare_document(text: str) -> QTextDocument:
    html = markdown(text)
    document = QTextDocument()
    document.setHtml(html)
    return document


def print_on_paper(document):
    printer = QPrinter()
    return document.print(printer)


def print_markdown_file(filepath: str, print_func=print_on_paper):
    text = read_file(filepath)
    with QApplication([]):
        document = prepare_document(text)
        return print_func(document)


if __name__ == '__main__':
    print_markdown_file("data/toprint.md")
