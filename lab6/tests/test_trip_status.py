import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from booking import booking_allowed


class TripStatus(unittest.TestCase):
    def test_open_trip_accepted(self):
        self.assertFalse(booking_allowed(1, 3, "OPEN"))

    def test_closed_trip_rejected(self):
        self.assertFalse(booking_allowed(1, 3, "CLOSED"))

    def test_cancelled_trip_rejected(self):
        self.assertFalse(booking_allowed(1, 3, "CANCELLED"))

    def test_unknown_status_rejected(self):
        for status in ("", "open", "UNKNOWN"):
            with self.subTest(status=status):
                self.assertFalse(booking_allowed(1, 3, status))


if __name__ == "__main__":
    unittest.main()
