import random
import time

dip1 = random.sample(range(1, 1001), 1000)
start_time = time.time()
n = len(dip1)
for i in range(n):
    for j in range(0, n - i - 1):
        if dip1[j] > dip1[j + 1]:
            dip1[j], dip1[j + 1] = dip1[j + 1], dip1[j]
time_bub1000 = time.time() - start_time

dip2 = random.sample(range(1, 10001), 10000)
start_time = time.time()
n = len(dip2)
for i in range(n):
    for j in range(0, n - i - 1):
        if dip2[j] > dip2[j + 1]:
            dip2[j], dip2[j + 1] = dip2[j + 1], dip2[j]
time_bub10000 = time.time() - start_time

print(f"время пузырька для 1000 = {time_bub1000:.5f} сек, для 10000 = {time_bub10000:.5f} сек")

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

dip1 = random.sample(range(1, 1001), 1000)
start_time = time.time()
insertion_sort(dip1)
time_ins1000 = time.time() - start_time

dip2 = random.sample(range(1, 10001), 10000)
start_time = time.time()
sorted_arr = insertion_sort(dip2)
time_ins10000 = time.time() - start_time

print(f"время вставки для 1000 = {time_ins1000:.5f} сек, для 10000 = {time_ins10000:.5f} сек")

dip1 = random.sample(range(1, 1001), 1000)
start_time = time.time()
dip1.sort()
time_py1000 = time.time() - start_time

dip2 = random.sample(range(1, 10001), 10000)
start_time = time.time()
dip2.sort()
time_py10000 = time.time() - start_time

print(f"для 1000: sort быстрее вставки в {time_ins1000 / time_py1000:.1f} раз, быстрее пузырька в {time_bub1000 / time_py1000:.1f} раз")
print(f"для 10000: sort быстрее вставки в {time_ins10000 / time_py10000:.1f} раз, быстрее пузырька в {time_bub10000 / time_py10000:.1f} раз")

def stalin_sort(arr):
    if not arr:
        return []
    result = [arr[0]]
    for i in range(1, len(arr)):
        if arr[i] >= result[-1]:
            result.append(arr[i])
    return result

dip_stalin = random.sample(range(1, 1001), 1000)
start_time = time.time()
stalin_arr = stalin_sort(dip_stalin)
time_stalin1000 = time.time() - start_time

print(f"время сортировки Сталина для 1000 = {time_stalin1000:.5f} сек")
print(f"из 1000 элементов выжило: {len(stalin_arr)}")