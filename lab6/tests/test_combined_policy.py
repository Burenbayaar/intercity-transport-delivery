import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from booking import booking_allowed


class CombinedPolicy(unittest.TestCase):
    def test_open_zero_seats_rejected(self):
        self.assertFalse(booking_allowed(0, 3, "OPEN"))

    def test_closed_positive_seats_rejected(self):
        self.assertFalse(booking_allowed(1, 3, "CLOSED"))

    def test_cancelled_negative_seats_rejected(self):
        self.assertFalse(booking_allowed(-1, 3, "CANCELLED"))

    def test_open_exact_capacity_accepted(self):
        self.assertTrue(booking_allowed(3, 3, "OPEN"))


if __name__ == "__main__":
    unittest.main()
