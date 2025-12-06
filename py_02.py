# from py_01 import greet
# greet('Vasa')
import time

start_time = time.time()  # Start the timer

# Code block to measure
for i in range(10000000000000000):
    x = i * i

end_time = time.time()  # End the timer

print(f"Time taken: {end_time - start_time} seconds")
