"""Lab 6 feature: only OPEN trips accept booking requests."""


def booking_allowed(seat_count: int, available_seats: int, trip_status: str) -> bool:
    """Check input types, available capacity and the trip's OPEN status."""
    if type(seat_count) is not int or type(available_seats) is not int:
        return False
    if not isinstance(trip_status, str) or available_seats < 0:
        return False
    return trip_status == "OPEN" and seat_count <= available_seats
