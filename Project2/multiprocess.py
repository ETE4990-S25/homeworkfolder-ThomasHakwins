from datetime import datetime, timedelta
from multiprocessing import Process, Queue
from math import factorial, isqrt
import time

# Prime checker from our assignment 
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
#https://www.datacamp.com/tutorial/fibonacci-sequence-python this was a good resource for the fibbanaci function stuff
def Fibbananci_Finder(prime_limit, queue):
    start = time.time()
    a, b = 0, 1
    while b < prime_limit and (time.time() - start) < 5:
        a, b = b, a + b
        if b > 1e8:
            queue.put("Fibonacci hit safety limit")
            return
    duration = time.time() - start
    queue.put(f"Fibonacci: {a}, Time: {duration:.10f}s")#10th decimal place for time bc percision matters :/

# Factorial function
#this was crazy in earlier iterations I was getting numbersw so large it was freezing my computer
def factorial_Finder(prime_limit, queue):
    start = time.time()
    n = 1
    result = 1
    while result < prime_limit and (time.time() - start) < 5:
        n += 1
        result = factorial(n)
        if result > 1e10:
            queue.put("Factorial too large")
            return
    duration = time.time() - start
    queue.put(f"Factorial: {factorial(n - 1)}, Base: {n - 1}, Time: {duration:.10f}s")


Adjustable_time = 3 # Set duration here for prime number calculation (in minutes)

if __name__ == '__main__':
    print(f"Finding highest prime in: {Adjustable_time} min...")

    start_total = time.time()
    prime = find_highest_prime(Adjustable_time)#set duration here for prime number calculation
    print(f"Prime number: {prime}")

    queue = Queue()
    p1 = Process(target=Fibbananci_Finder, args=(prime, queue))
    p2 = Process(target=factorial_Finder, args=(prime, queue))

    print("Starting parallel processes...")
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    while not queue.empty():
        print(queue.get())

    print(f"Total time: {time.time() - start_total:.10f}s")

####Results####

# Finding highest prime in: 3 min...
# Prime number: 18955583
# Starting parallel processes...
# Fibonacci: 14930352, Time: 0.0000092983s
# Factorial: 3628800, Base: 10, Time: 0.0000054836s
# Total time: 180.1191313267s