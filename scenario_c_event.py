# Scenario C – Event Registration
# Problem: Event has only 1 place remaining (remaining_places = 1).
# Three students try to register concurrently. Mutex prevents overbooking.

import threading
import time

remaining_places = 1
reg_lock = threading.Lock()
registered_students = []

def register_student(student_name):
    global remaining_places, registered_students
    print(f"[{student_name}] Submitting event registration form...")
    
    with reg_lock:
        if remaining_places > 0:
            print(f"[{student_name}] Seat reserved. Validating registration details...")
            time.sleep(0.5)
            remaining_places -= 1
            registered_students.append(student_name)
            print(f"--> [{student_name}] REGISTRATION CONFIRMED! Remaining places: {remaining_places}")
        else:
            print(f"--> [{student_name}] REGISTRATION CLOSED: Event is at full capacity! Remaining: {remaining_places}")

students = ["Student-101", "Student-102", "Student-103"]
threads = [threading.Thread(target=register_student, args=(s,)) for s in students]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"\nFinal Remaining Capacity: {remaining_places}")
print(f"Registered Attendees: {registered_students}")
