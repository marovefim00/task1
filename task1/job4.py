import random

dip = random.sample(range(1, 10000001), 10000000)
target = random.choice(dip)

def line_search_count(arr, item_to_find):
    steps = 0
    for element in arr:
        steps += 1
        if element == item_to_find:
            return steps
    return steps #линейная проверка

dip_sorted = sorted(dip)

def binary_search_count(arr, item_to_find):
    steps = 0
    low = 0
    high = len(arr) - 1

    while low <= high:
        steps += 1
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item_to_find:
            return steps
        if guess > item_to_find:
            high = mid - 1
        else:
            low = mid + 1
    return steps #бинарный поиск

print(f"искомое число: {target}")
print(f"шагов линейного поиска: {line_search_count(dip_sorted, target)}")
print(f"шагов бинарного поиска: {binary_search_count(dip_sorted, target)}")
print("наглядный пример" + "\nбинарный поиск проверяет весь доступный диапазон за шаг")
