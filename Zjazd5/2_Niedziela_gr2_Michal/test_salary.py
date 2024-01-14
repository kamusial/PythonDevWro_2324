import pytest

from salary import generate_salary_report, Employee


def test_salary():
    employees = [
        Employee("Bartosz", 100, 40),
        Employee("Anna", 120, 50)
    ]
    report = generate_salary_report(employees)
    assert type(report) is dict
    # Możemy sprawdzać każdą wartość pojedynczo:
    assert report["Bartosz"]["salary"] == 4000
    # Albo od razu cały output z funkcji:
    assert report == {
        'Bartosz': {
            'salary': 4000,
            'hours_worked': 40
        },
        'Anna': {
            'salary': 6600.0,
            'hours_worked': 50
        },
        'total_expenses': 10600.0
    }


def test_empty_list():
    with pytest.raises(ValueError, match="Employee list is empty"):
        generate_salary_report([])
