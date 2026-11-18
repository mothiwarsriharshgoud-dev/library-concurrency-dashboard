# Exercise 2: Sequential Seat Booking without Concurrency
# Demonstrates normal single-request logic where functions execute one after another

seat = "Available"

def book_seat(passenger):
    global seat
    if seat == "Available":
        seat = "Booked"
        print(passenger, "booking successful")
    else:
        print(passenger, "seat unavailable")

book_seat("P1")
book_seat("P2")

print("Final seat status:", seat)
