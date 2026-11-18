# Scenario E – Library Last Copy
# Problem: One physical copy of a book is available (available_copies = 1).
# Two users request it concurrently. Prevent duplicate issue.

import threading
import time

available_copies = 1
book_title = "Operating System Concepts (Silberschatz)"
library_lock = threading.Lock()
issued_to = []

def borrow_book(user_name):
    global available_copies, issued_to
    print(f"[{user_name}] Checking catalog for '{book_title}'...")
    
    with library_lock:
        if available_copies > 0:
            print(f"[{user_name}] Copy found on shelf. Processing checkout barcode...")
            time.sleep(0.5)
            available_copies -= 1
            issued_to.append(user_name)
            print(f"--> [{user_name}] BOOK ISSUED! Remaining copies: {available_copies}")
        else:
            print(f"--> [{user_name}] UNAVAILABLE: All copies currently checked out!")

u1 = threading.Thread(target=borrow_book, args=("User-Alice",))
u2 = threading.Thread(target=borrow_book, args=("User-Bob",))

u1.start()
u2.start()

u1.join()
u2.join()

print(f"\nFinal Available Copies: {available_copies}")
print(f"Borrowed by: {issued_to}")
