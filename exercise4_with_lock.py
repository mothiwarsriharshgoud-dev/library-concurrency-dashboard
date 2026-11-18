# Exercise 4 (Enhancement): Using Python's 'with lock:' context manager
# Safer shorthand that automatically releases the lock even if an exception occurs

import threading
import time

seat = "Available"
lock = threading.Lock()

def book_seat(passenger):
    global seat
    with lock:
        if seat == "Available":
            print(f"{passenger} found the seat available")
            time.sleep(1)
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
