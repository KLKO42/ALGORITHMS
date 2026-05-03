import time
import random

def task4(n):
    table=[]
    for i in range(1, n+1):
        row=[]
        for j in range(1, n+1):
            row.append(i*j)
        table.append(row)
    return table

def measure_time(func, data):
    start = time.perf_counter()
    func(data)
    end = time.perf_counter()
    return end - start

if __name__ == '__main__':
    #тут o(n^2), => беру меньшие значения, чтобы не было так долго
    sizes = [100, 200, 300, 400, 500]
    for n in sizes:
        t = measure_time(task4, n)
        print(f"{n} {t:.6f}")
