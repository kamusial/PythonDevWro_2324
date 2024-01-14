from salary import generate_salary_report, Employee


def test_salary():
    bartek = Employee("Bartosz", 100, 40)
    report = generate_salary_report([bartek])
    assert type(report) is dict
    # Możemy sprawdzać każdą wartość pojedynczo:
    assert report["Bartosz"]["salary"] == 4000
    # Albo od razu cały output z funkcji:
    assert report == {
        'Bartosz': {
            'salary': 4000,
            'hours_worked': 40
        },
        'total_expenses': 4000.0
    }
