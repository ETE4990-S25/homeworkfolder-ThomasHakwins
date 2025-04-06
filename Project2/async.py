from datetime import datetime, timedelta
import asyncio
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

# Find highest prime within a time limit (in minutes)
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
def Fibbanaci_Finder(prime_limit):
    start = time.time()
    a, b = 0, 1
    while b < prime_limit and (time.time() - start) < 5:
        a, b = b, a + b
        if b > 1e8:
            return "Fibonacci hit safety limit"
    duration = time.time() - start
    return f"Fibonacci: {a}, Time: {duration:.10f}s"

# Factorial function 
def factorial_Finder(prime_limit):
    start = time.time()
    n = 1
    result = 1
    while result < prime_limit and (time.time() - start) < 5:
        n += 1
        result = factorial(n)
        if result > 1e8:
            return "Factorial hit safety limit"
    duration = time.time() - start
    return f"Factorial: {factorial(n - 1)}, Base: {n - 1}, Time: {duration:.10f}s"




Adjustable_time = 3 # Set duration here for prime number calculation (in minutes)

# Async version of the main run
async def main():
    print(f"Finding highest prime in: {Adjustable_time} min...")
    start_total = time.time()
    prime = await asyncio.to_thread(find_highest_prime, Adjustable_time)
    print(f"Prime number: {prime}")

    # Run both fib and fact in parrallel
    fib_result = await asyncio.to_thread(Fibbanaci_Finder, prime)
    fact_result = await asyncio.to_thread(factorial_Finder, prime)

    print(fib_result)
    print(fact_result)

    print(f"Total time: {time.time() - start_total:.10f}s")

if __name__ == '__main__':
    asyncio.run(main())


###Results######

# Finding highest prime in: 3 min...
# Prime number: 18288293
# Fibonacci: 14930352, Time: 0.0000195503s
# Factorial: 3628800, Base: 10, Time: 0.0000081062s
# Total time: 180.0041408539s