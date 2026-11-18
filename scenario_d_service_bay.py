# Scenario D – Service Bay Time Slot
# Problem: One service bay is available at 2:00 PM.
# Two customers request it at nearly the same time. Prevent duplicate booking.

import threading
import time

service_bay = {
    "bay_id": "Bay-4",
    "time_slot": "2:00 PM",
    "status": "Available",
    "assigned_to": None
}
bay_lock = threading.Lock()

def book_service_bay(customer_name):
    global service_bay
    print(f"[{customer_name}] Requesting Service Bay at 2:00 PM...")
    
    with bay_lock:
        if service_bay["status"] == "Available":
            print(f"[{customer_name}] Bay available. Assigning bay...")
            time.sleep(0.5)
            service_bay["status"] = "Reserved"
            service_bay["assigned_to"] = customer_name
            print(f"--> [{customer_name}] SUCCESS: Service bay reserved at 2:00 PM")
        else:
            print(f"--> [{customer_name}] REJECTED: Service bay already booked by {service_bay['assigned_to']}")

c1 = threading.Thread(target=book_service_bay, args=("Customer-1",))
c2 = threading.Thread(target=book_service_bay, args=("Customer-2",))

c1.start()
c2.start()

c1.join()
c2.join()

print("\nFinal Bay Status:", service_bay)
