"""Ten test może być niestabilny!
Zależy od tego, czy strona api.nbp działa ORAZ od tego czy mamy internet

Uzyskanie niezależności od internetu:
Priorytet 1: dependency injection
Priorytet 2: dedykowana biblioteka do mockowania httpx (pytest-httpx)
Priorytet 3: import mock -> MagicMock, patch

"""
from rates.get_rate import get_rate


class UdawanyInternet:
    def get(self, *args):
        class Response:
            def json(self):
                return {"table": "A", "currency": "euro", "code": "EUR",
                        "rates": [{"no": "238/A/NBP/2023", "effectiveDate": "2023-12-08", "mid": 4.3303}]}
        return Response()


def test_get_rate():
    result = get_rate("EUR", UdawanyInternet())
    assert result == 4.3303
