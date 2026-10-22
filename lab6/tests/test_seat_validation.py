import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from booking import booking_allowed


class SeatValidation(unittest.TestCase):
    def test_zero_seats_rejected(self):
        self.assertFalse(booking_allowed(0, 3, "OPEN"))

    def test_negative_seats_rejected(self):
        self.assertFalse(booking_allowed(-1, 3, "OPEN"))

    def test_exact_capacity_accepted(self):
        self.assertTrue(booking_allowed(3, 3, "OPEN"))

    def test_no_available_seats(self):
        self.assertFalse(booking_allowed(1, 0, "OPEN"))

    def test_one_seat_over_capacity(self):
        self.assertFalse(booking_allowed(4, 3, "OPEN"))


if __name__ == "__main__":
    unittest.main()
