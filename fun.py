import time
for i in range(11):
    print(f"\rProgress: {i*10}%", end="",flush=True)
    time.sleep(0.5)
print() # Print a final newline to move the cursor to the next line
