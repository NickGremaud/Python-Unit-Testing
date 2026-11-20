import unittest
from datetime import datetime


def validate_symbol(symbol):
    return (
        isinstance(symbol, str)
        and 1 <= len(symbol) <= 7
        and symbol.isalpha()
        and symbol.isascii()
        and symbol.isupper()
    )


def validate_chart_type(chart_type):
    return isinstance(chart_type, str) and chart_type in ("1", "2")


def validate_time_series(time_series):
    return isinstance(time_series, str) and time_series in ("1", "2", "3", "4")


def validate_start_date(start_date):
    if not isinstance(start_date, str):
        return False

    try:
        parsed_date = datetime.strptime(start_date, "%Y-%m-%d")
        return parsed_date.strftime("%Y-%m-%d") == start_date
    except ValueError:
        return False


def validate_end_date(end_date):
    if not isinstance(end_date, str):
        return False

    try:
        parsed_date = datetime.strptime(end_date, "%Y-%m-%d")
        return parsed_date.strftime("%Y-%m-%d") == end_date
    except ValueError:
        return False


class TestStockInputs(unittest.TestCase):

    def test_valid_symbol(self):
        self.assertTrue(validate_symbol("AAPL"))
        self.assertTrue(validate_symbol("A"))
        self.assertTrue(validate_symbol("ABCDEFG"))

    def test_invalid_symbol(self):
        self.assertFalse(validate_symbol("aapl"))
        self.assertFalse(validate_symbol("AAPL123"))
        self.assertFalse(validate_symbol("ABCDEFGH"))
        self.assertFalse(validate_symbol(""))
        self.assertFalse(validate_symbol("AA PL"))

    def test_valid_chart_type(self):
        self.assertTrue(validate_chart_type("1"))
        self.assertTrue(validate_chart_type("2"))

    def test_invalid_chart_type(self):
        self.assertFalse(validate_chart_type("3"))
        self.assertFalse(validate_chart_type("0"))
        self.assertFalse(validate_chart_type("12"))
        self.assertFalse(validate_chart_type("bar"))
        self.assertFalse(validate_chart_type(""))
        self.assertFalse(validate_chart_type(1))

    def test_valid_time_series(self):
        self.assertTrue(validate_time_series("1"))
        self.assertTrue(validate_time_series("2"))
        self.assertTrue(validate_time_series("3"))
        self.assertTrue(validate_time_series("4"))

    def test_invalid_time_series(self):
        self.assertFalse(validate_time_series("0"))
        self.assertFalse(validate_time_series("5"))
        self.assertFalse(validate_time_series("12"))
        self.assertFalse(validate_time_series("daily"))
        self.assertFalse(validate_time_series(""))
        self.assertFalse(validate_time_series(1))

    def test_valid_start_date(self):
        self.assertTrue(validate_start_date("2026-11-19"))
        self.assertTrue(validate_start_date("2026-01-05"))
        self.assertTrue(validate_start_date("2024-02-29"))

    def test_invalid_start_date(self):
        self.assertFalse(validate_start_date("2026-13-19"))
        self.assertFalse(validate_start_date("2026-02-30"))
        self.assertFalse(validate_start_date("2026-1-5"))
        self.assertFalse(validate_start_date("11-19-2026"))
        self.assertFalse(validate_start_date(""))
        self.assertFalse(validate_start_date(20261119))

    def test_valid_end_date(self):
        self.assertTrue(validate_end_date("2026-11-19"))
        self.assertTrue(validate_end_date("2026-12-31"))
        self.assertTrue(validate_end_date("2024-02-29"))

    def test_invalid_end_date(self):
        self.assertFalse(validate_end_date("2026-13-19"))
        self.assertFalse(validate_end_date("2026-02-30"))
        self.assertFalse(validate_end_date("2026-1-5"))
        self.assertFalse(validate_end_date("11-19-2026"))
        self.assertFalse(validate_end_date(""))
        self.assertFalse(validate_end_date(20261119))        


if __name__ == "__main__":
    unittest.main()        