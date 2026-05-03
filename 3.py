import time
import random

def task3(arr, target):
    left=0
    right=len(arr)-1
    while left<=right:
        mid = (left+right)//2
        if arr[mid] == target: return mid #всё нашли
        elif arr[mid] < target: left = mid + 1 #надо двигаться правее
        else: right = mid - 1 #или наоборот в противном случае 
    return -1

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
        arr.sort()  #бинарный поиск работает только с отсортированным массивом
        target = arr[-1]  
        t = measure_time(task3, arr, target)
        print(f"{n} {t:.6f}")
