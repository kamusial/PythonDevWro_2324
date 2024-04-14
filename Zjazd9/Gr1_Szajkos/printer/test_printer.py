from unittest.mock import patch

from .printer import print_markdown_file, QTextDocument


def test_print():
    with patch.object(QTextDocument, "print", lambda self, printer: QTextDocument.toPlainText(self)):
        result = print_markdown_file("data/toprint.md")
    assert result == "Python\nis\nok"


def test_print_dependency_injection():
    result = print_markdown_file("data/toprint.md",
                                 print_func=QTextDocument.toPlainText)
    assert result == "Python\nis\nok"
