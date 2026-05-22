print(f"строки 'Привет': {hash('Привет')}")
print(f"числа 100: {hash(100)}")
print(f"кортеж (1, 2): {hash((1, 2))}")

my_dict = {}
valid_key = (1, 2)
invalid_key = [1, 2]

my_dict[valid_key] = "это сработает"
print(f"словарь с кортежем: {my_dict}")

try:
    my_dict[invalid_key] = "вызов ошибки!"
except TypeError as error:
    print(f"использование списка вызывает ошибку: {error}\n")

class SimpleHashMap:
    def __init__(self, size=5):
        self.size = size
        self.table = [[]for _ in range(self.size)]
    # таблица из 5и ячеек
    def _get_hash(self, key):
        return abs(hash(key)) % self.size
    # кидаем ограничения на кол-во индексов

    def put(self, key, value):
        index = self._get_hash(key) #поиск
        bucket = self.table[index] #выбор

        for kv_pair in bucket:
            if kv_pair[0] == key:
                kv_pair[1] = value
                return
    # проверка дублик индекса

        bucket.append([key, value])

    def get(self, key):
        index = self._get_hash(key)
        bucket = self.table[index]
    #поиск ячейки по хеш

        for kv_pair in bucket:
            if kv_pair[0] == key:
                return kv_pair[1]
    # поиск ключа
        raise KeyError(f"ключ '{key}' не найден")

my_dict = SimpleHashMap(size = 5)
my_dict.put("кот", "мяу")
my_dict.put("пес", "гав")
my_dict.put("корова", "муу")

print("=== СОДЕРЖИМОЕ НАШЕЙ ХЕШ-ТАБЛИЦЫ ===")
for idx, bucket in enumerate(my_dict.table):
    print(f"ячейка №{idx}: {bucket}")

print("\n=== ПОЛУЧЕНИЕ ЗНАЧЕНИЙ ===")
print(f"Что говорит кот? -> {my_dict.get('кот')}")
print(f"Что говорит пес? -> {my_dict.get('пес')}")
