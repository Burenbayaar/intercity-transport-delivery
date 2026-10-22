import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from booking import booking_allowed


class SharedRules(unittest.TestCase):
    def test_valid_request(self):
        self.assertTrue(booking_allowed(1, 2, "OPEN"))

    def test_over_capacity(self):
        self.assertFalse(booking_allowed(3, 2, "OPEN"))

    def test_invalid_seat_types(self):
        for value in (True, 1.5, "1", None):
            with self.subTest(value=value):
                self.assertFalse(booking_allowed(value, 2, "OPEN"))

    def test_invalid_capacity(self):
        for value in (-1, True, 2.5, "2", None):
            with self.subTest(value=value):
                self.assertFalse(booking_allowed(1, value, "OPEN"))

    def test_invalid_status_type(self):
        self.assertFalse(booking_allowed(1, 2, None))


if __name__ == "__main__":
    unittest.main()
