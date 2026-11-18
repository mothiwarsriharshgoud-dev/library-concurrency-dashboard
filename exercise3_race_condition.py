# Exercise 3: Reproducing a Race Condition (Unsafe Version - No Mutex)
# Demonstrates how concurrent threads checking before updating cause duplicate bookings

import threading
import time

seat = "Available"

def book_seat(passenger):
    global seat
    if seat == "Available":
        print(f"{passenger} found the seat available")
        time.sleep(1)  # Teaching delay to expose race condition
        seat = "Booked"
        print(f"{passenger} booking successful")
    else:
        print(f"{passenger} seat unavailable")

t1 = threading.Thread(target=book_seat, args=("P1",))
t2 = threading.Thread(target=book_seat, args=("P2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final seat status:", seat)
