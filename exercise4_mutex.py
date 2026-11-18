# Exercise 4: Protecting the Critical Section with a Mutex
# Uses threading.Lock() with acquire() and release()

import threading
import time

seat = "Available"
lock = threading.Lock()

def book_seat(passenger):
    global seat
    lock.acquire()  # Acquire lock to enter critical section
    try:
        if seat == "Available":
            print(f"{passenger} found the seat available")
            time.sleep(1)  # Protected work inside critical section
            seat = "Booked"
            print(f"{passenger} booking successful")
        else:
            print(f"{passenger} seat unavailable")
    finally:
        lock.release()  # Always release lock for waiting threads

t1 = threading.Thread(target=book_seat, args=("P1",))
t2 = threading.Thread(target=book_seat, args=("P2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Final seat status:", seat)
