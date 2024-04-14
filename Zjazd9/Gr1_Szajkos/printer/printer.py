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


def print_markdown_file(filepath: str):
    text = read_file(filepath)
    with QApplication([]):
        document = prepare_document(text)
        printer = QPrinter()
        document.print(printer)


if __name__ == '__main__':
    print_markdown_file("data/toprint.md")
