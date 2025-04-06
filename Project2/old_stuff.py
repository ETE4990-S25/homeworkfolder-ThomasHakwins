import time
import threading
import multiprocessing
import asyncio

Amount_oftime = 5  # Time limit in seconds
def main():
    print("Running Multiprocessing...")
    multiprocessing_prime()

    print("Running Threading...")
    threading_prime()

    print("Running Async...")
    asyncio.run(async_prime())


#prime checker from lecture thingy
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# Function that checks if its a prime number
def find_highest_prime(limit_time, result):
    start_time = time.time()
    num = 0
    highest_prime = 0
    while time.time() - start_time < limit_time:
        if is_prime(num):
            highest_prime = num
        num += 1
    result[0] = highest_prime


# Multiprocessing run
def multiprocessing_prime():
    start_time = time.time()
    print(f"Multiprocessing start time: {time.ctime(start_time)}")
    
    manager = multiprocessing.Manager()
    result = manager.list([0])
    process = multiprocessing.Process(target=find_highest_prime, args=(Amount_oftime, result))
    process.start()
    process.join()
    
    duration = time.time() - start_time
    print(f"Multiprocessing highest prime: {result[0]}")
    print(f"Multiprocessing duration: {duration:.2f} seconds\n")


# Threading run
def threading_prime():
    start_time = time.time()
    print(f"Threading start time: {time.ctime(start_time)}")
    
    result = [0] 

    thread = threading.Thread(target=find_highest_prime, args=(Amount_oftime, result))
    thread.start()
    thread.join()
    
    duration = time.time() - start_time
    print(f"Threading highest prime: {result[0]}")
    print(f"Threading duration: {duration:.2f} seconds\n")


# Async run 
    start_time = time.time()
    print(f"Async start time: {time.ctime(start_time)}")
    
    num = 0

    highest_prime = 0

    while time.time() - start_time < Amount_oftime:
        if is_prime(num):
            highest_prime = num
        num += 1
    
    duration = time.time() - start_time
    print(f"Async highest prime: {highest_prime}")
    print(f"Async duration: {duration:.2f} seconds\n")


if __name__ == "__main__":
    main()
#this made me want to die
#still need the fibonacci and factorials but this is the main part of the code

