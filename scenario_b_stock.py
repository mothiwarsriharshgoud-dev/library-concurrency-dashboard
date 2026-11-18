# Scenario B – Last Product in Stock
# Problem: Store has stock = 1 for a product.
# Three customers try to purchase it concurrently. Prevent duplicate sale.

import threading
import time

stock = 1
stock_lock = threading.Lock()

def purchase_product(customer_name):
    global stock
    print(f"[{customer_name}] Browsing product (Current stock: {stock})...")
    
    with stock_lock:
        if stock > 0:
            print(f"[{customer_name}] Stock verified available. Processing checkout...")
            time.sleep(0.5)
            stock -= 1
            print(f"--> [{customer_name}] ORDER SUCCESS: Item purchased! Remaining stock: {stock}")
        else:
            print(f"--> [{customer_name}] ORDER FAILED: Out of stock! (Remaining: {stock})")

customers = ["Customer-A", "Customer-B", "Customer-C"]
threads = [threading.Thread(target=purchase_product, args=(c,)) for c in customers]

for t in threads:
    t.start()
for t in threads:
    t.join()

print(f"\nFinal Stock Value: {stock}")
