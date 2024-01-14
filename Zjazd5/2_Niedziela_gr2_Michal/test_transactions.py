import pytest

from transactions import process_transactions


def test_process_transactions():
    result = process_transactions([{"amount": 5, "type": "credit"}, {"amount": 5, "type": "credit"}])
    assert result == 10
    print(result)


def test_amount():
    result = process_transactions([{"amount": 0, "type": "debit"}])
    assert result == 0


def test_debit():
    result = process_transactions([{"amount": 5, "type": "credit"}, {"amount": 2, "type": "debit"}])
    assert result == 3


def test_process_transactions_bad():
    with pytest.raises(ValueError):
        process_transactions("banan")


def test_invalid_transactions_type():
    with pytest.raises(ValueError):
        process_transactions([{"amount": 5, "type": "not_credit"}])


def test_transactions_empty():
    with pytest.raises(ValueError):
        process_transactions("")


def test_transactions_amount_empty():
    with pytest.raises(ValueError):
        process_transactions([{"amount": "", "type": ""}])


def test_transactions_type_missing():
    with pytest.raises(ValueError):
        process_transactions([{"amount": 5}])


def test_transactions_insufficient_funds():
    with pytest.raises(ValueError):
        process_transactions([{"amount": 100000, "type": "debit"}])


def test_transactions_amount_negative_credit():
    with pytest.raises(ValueError):
        process_transactions([{"amount": -100, "type": "credit"}])


def test_transactions_amount_negative_debit():
    with pytest.raises(ValueError, match=r"Insufficient funds") as pytest_object:
        process_transactions([{"amount": 100, "type": "debit"}])
    assert isinstance(pytest_object.value, Exception)
    assert type(pytest_object.value) is ValueError
