"""Lab 6 starter for a pure booking-eligibility check.

This is a teaching scaffold: feature branches add the missing positive-seat
and OPEN-trip rules. It does not reserve seats or write to a database.
"""


def booking_allowed(seat_count: int, available_seats: int, trip_status: str) -> bool:
    """Check the shared input rules; feature branches complete the policy."""
    if type(seat_count) is not int or type(available_seats) is not int:
        return False
    if not isinstance(trip_status, str) or available_seats < 0:
        return False
    return seat_count <= available_seats
