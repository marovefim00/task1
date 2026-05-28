import random
import time


start_time1 = time.perf_counter()

classroom = {
    "Симба": {"age" : 14,"grade": set(random.sample(range(1, 6), 3))},
    "Ариэль": {"age" : 13,"grade": set(random.sample(range(1, 6), 3))},
    "Аладдин": {"age" : 14,"grade": set(random.sample(range(1, 6), 3))},
    "Мулан": {"age" : 15,"grade": set(random.sample(range(1, 6), 3))},
    "Балу": {"age" : 14,"grade": set(random.sample(range(1, 6), 3))}
} #прмер множества

for name, info in classroom.items():
    if 5 in info["grade"]:
        print("наши отличники: " + name)
end_time1 = time. perf_counter() - start_time1
print(f"время выполнения множества: {end_time1:.6f} сек.")

start_time2 = time.perf_counter()
classroom = {
"Симба": {"age" : 14,"grade": [random.randint(1, 5) for _ in range(3)]},
    "Ариэль": {"age" : 13,"grade": [random.randint(1, 5) for _ in range(3)]},
    "Аладдин": {"age" : 14,"grade": [random.randint(1, 5) for _ in range(3)]},
    "Мулан": {"age" : 15,"grade": [random.randint(1, 5) for _ in range(3)]},
    "Балу": {"age" : 14,"grade": [random.randint(1, 5) for _ in range(3)]}
} #прмер списка

for name, info in classroom.items():
    if 5 in info["grade"]:
        print("наши отличники: " + name)
end_time2 = time.perf_counter() - start_time2
print(f"время выполнения списка: {end_time2:.6f} сек.")
print("я пытался показать разниц, но блок размером с космическую частицу, поэтому вот просто время операций")
