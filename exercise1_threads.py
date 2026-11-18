# Exercise 1: Creating and Running Two Threads
# Department of CSE | School of CS & AI - SR University
# Course: Operating Systems and Computer Networks (25CAI402PC203)

import threading

def task(name):
    print(name, "is running")

# Creating threads
t1 = threading.Thread(target=task, args=("Thread-1",))
t2 = threading.Thread(target=task, args=("Thread-2",))

# Starting execution
t1.start()
t2.start()

# Waiting for completion
t1.join()
t2.join()

print("Main program finished")
