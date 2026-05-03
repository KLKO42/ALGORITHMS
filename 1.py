import time
import random

def task1(arr, target): #проверка наличия элемента в массиве
    for x in arr:
        if x == target:
            return True
    return False

def measure_time(func, data, target):
    start = time.perf_counter()
    func(data, target)
    end = time.perf_counter()
    return end - start

def generate_array(n): 
    arr = []
    for i in range(n):
        arr.append(random.randint(0, 10000))
    return arr

if __name__ == '__main__':
    sizes = [100, 1000, 5000, 10000]
    for n in sizes:
        arr = generate_array(n)
        target = arr[-1]  # по последнему эдементу
        t = measure_time(task1, arr, target)
        print(f"{n} {t:.6f}")
