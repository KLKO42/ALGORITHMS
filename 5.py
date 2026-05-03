import time
import random
import sys

def task5(arr): #сортировка вставками
    arr_copy=arr.copy() #на всякий случай
    for i in range(1, len(arr_copy)):
        key=arr_copy[i]
        j=i-1
        while j>=0 and arr_copy[j]>key:
            arr_copy[j + 1]=arr_copy[j]
            j-=1
        arr_copy[j+1]=key
    return arr_copy

def measure_time_and_memory(func, data): #и время и память вместе
    start = time.perf_counter()
    result = func(data)
    end = time.perf_counter()
    time_taken=end-start
    
    memory=sys.getsizeof(result)
    for item in result:
        memory+=sys.getsizeof(item)
    return time_taken, memory

def generate_array(n):
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        t, mem = measure_time_and_memory(task5, arr)
        print(f"{n}  {t:.6f}  {mem}")
