"""Lab 6 merged policy: positive seats, enough capacity and an OPEN trip.

This pure check does not reserve seats or prevent concurrent bookings.
A real system must recheck and reserve seats inside a database transaction.
"""


def booking_allowed(seat_count: int, available_seats: int, trip_status: str) -> bool:
    """Return whether a request satisfies both features and shared rules."""
    if type(seat_count) is not int or type(available_seats) is not int:
        return False
    if not isinstance(trip_status, str) or available_seats < 0:
        return False
    return trip_status == "OPEN" and 0 < seat_count <= available_seats




Нийлсэн нөхцөлийг шалгалаа. Аялал OPEN байх, хүссэн суудлын тоо эерэг байх, сул суудлаас хэтрэхгүй байх гурван шаардлагыг зэрэг хадгалсан байна. CLOSED аяллын багтаамж хүрэлцэж байсан ч захиалгыг хориглоно.
