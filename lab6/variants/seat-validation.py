"""Lab 6 feature: reject zero or negative requested seat counts."""


def booking_allowed(seat_count: int, available_seats: int, trip_status: str) -> bool:
    """Check input types, available capacity and positive requested seats."""
    if type(seat_count) is not int or type(available_seats) is not int:
        return False
    if not isinstance(trip_status, str) or available_seats < 0:
        return False
    return 0 < seat_count <= available_seats
