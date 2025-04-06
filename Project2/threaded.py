from datetime import datetime, timedelta
from threading import Thread
from math import factorial, isqrt
import queue
import time

# from lecture assignment page thing
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

# Find highest prime in a time limit (in minutes)
def find_highest_prime(limit_minutes):
    end_time = datetime.now() + timedelta(minutes=limit_minutes)
    num = 0 #starts from 0 bc it was asked for in the assignment
    highest = 0
    while datetime.now() < end_time:
        if is_prime(num):
            highest = num
        num += 1
    return highest

# Fibonacci function
def Fibbananci_Finder(prime_limit, output_queue):
    start = time.time()
    a, b = 0, 1
    while b < prime_limit and (time.time() - start) < 5:
        a, b = b, a + b
        if b > 1e8:
            output_queue.put("Fibonacci hit safety limit")
            return
    duration = time.time() - start
    output_queue.put(f"Fibonacci: {a}, Time: {duration:.10f}s")

# Factorial function
def factorial_Finder(prime_limit, output_queue):
    start = time.time()
    n = 1
    result = 1
    while result < prime_limit and (time.time() - start) < 5:
        n += 1
        result = factorial(n)
        if result > 1e8:
            output_queue.put("Factorial hit safety limit")
            return
    duration = time.time() - start
    output_queue.put(f"Factorial: {factorial(n - 1)}, Base: {n - 1}, Time: {duration:.10f}s")


Adjustable_time = 3 # Set duration here for prime number calculation (in minutes)


if __name__ == '__main__':
    print(f"Finding highest prime in: {Adjustable_time} min...")
    start_total = time.time()
    prime = find_highest_prime(Adjustable_time)
    print(f"Prime number: {prime}")

    output_queue = queue.Queue()
    t1 = Thread(target=Fibbananci_Finder, args=(prime, output_queue))
    t2 = Thread(target=factorial_Finder, args=(prime, output_queue))

    print("Starting threads...")
    t1.start()
    t2.start()
    t1.join()
    t2.join()

    while not output_queue.empty():
        print(output_queue.get())

    print(f"Total time: {time.time() - start_total:.10f}s")

###Results###
# Finding highest prime in: 3 min...
# Prime number: 18829021
# Starting threads...
# Fibonacci: 14930352, Time: 0.0000126362s
# Factorial: 3628800, Base: 10, Time: 0.0000066757s
# Total time: 180.0021021366s