# Scenario A – Hospital Appointment Slot
# Problem: One doctor has one available 10:00 AM slot.
# Three patients request the same slot concurrently.
# Mutex ensures only one patient receives the appointment.

import threading
import time

appointment_slot = {
    "time": "10:00 AM",
    "doctor": "Dr. Smith",
    "booked_by": None,
    "status": "Available"
}
slot_lock = threading.Lock()

def request_appointment(patient_name):
    global appointment_slot
    print(f"[{patient_name}] Requesting appointment for {appointment_slot['time']}...")
    
    slot_lock.acquire()
    try:
        if appointment_slot["status"] == "Available":
            print(f"[{patient_name}] Found slot available! Confirming booking...")
            time.sleep(0.5)
            appointment_slot["status"] = "Booked"
            appointment_slot["booked_by"] = patient_name
            print(f"--> [{patient_name}] SUCCESS: Appointment confirmed with {appointment_slot['doctor']} at {appointment_slot['time']}")
        else:
            print(f"--> [{patient_name}] REJECTED: Slot already booked by {appointment_slot['booked_by']}")
    finally:
        slot_lock.release()

patients = ["Patient-1 (Alice)", "Patient-2 (Bob)", "Patient-3 (Charlie)"]
threads = [threading.Thread(target=request_appointment, args=(p,)) for p in patients]

for t in threads:
    t.start()
for t in threads:
    t.join()

print("\nFinal Hospital Slot Status:", appointment_slot)
