import time
import threading
import multiprocessing
import asyncio
import nest_asyncio

def main():
    print("Running Multiprocessing...")
    multiprocessing_prime()
    
    print("Running Threading...")
    threading_prime()
    
    print("Running Async...")
    nest_asyncio.apply()  # Fixes asyncio issue in Jupyter
    asyncio.get_event_loop().run_until_complete(async_prime())


# Prime-checking function
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# find the highest prim
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
    manager = multiprocessing.Manager()
    result = manager.list([0])
    process = multiprocessing.Process(target=find_highest_prime, args=(180, result))
    process.start()
    process.join()
    print(f"Multiprocessing highest prime: {result[0]}")

# Threading run
def threading_prime():
    result = [0]  # Mutable list for shared memory
    thread = threading.Thread(target=find_highest_prime, args=(180, result))
    thread.start()
    thread.join()
    print(f"Threading highest prime: {result[0]}")

# Async run
async def async_prime():
    start_time = time.time()
    num = 0
    highest_prime = 0
    while time.time() - start_time < 180:
        if is_prime(num):
            highest_prime = num
        num += 1
    print(f"Async highest prime: {highest_prime}")

# Run all methods and print results
def main():
    print("Running Multiprocessing...")
    multiprocessing_prime()
    
    print("Running Threading...")
    threading_prime()
    
    print("Running Async...")
    asyncio.run(async_prime())

if __name__ == "__main__":
    main()

    