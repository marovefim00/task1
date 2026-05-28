import random
import time

start_time = time.perf_counter()
num=[]

for i in range(10):
    d = random.randint(1,10)
    num.append(d)
num_sort1 = sorted(num)
num_sort2 = sorted(num, reverse=True)
stop_time = time.perf_counter()
minimum = min(num)
maximum = max(num)
print("список" , num, "\n min.", minimum , "max", maximum, "\n время выполнения", (stop_time - start_time) * 10000, )
print("первый способ", num_sort1, "второй способ", num_sort2)