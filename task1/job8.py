import time

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(start_node):
    current = start_node
    chain = []
    while current is not None:
        chain.append(current.data)
        current = current.next
    print("текущий список:", "-".join(chain))

def add_node(start_node, new_node):
    current = start_node
    while current.next is not None:
        current = current.next
    current.next = new_node

def delete_node(start_node, name_to_delete):
    print(f"удаляем: {name_to_delete}")
    if start_node.data == name_to_delete:
        return start_node.next

    current = start_node
    while current.next is not None:
        if current.next.data == name_to_delete:
            current.next = current.next.next
            return start_node
        current = current.next
    return start_node

def find_node(start_node, name_to_find):
    current = start_node
    while current is not None:
        if current.data == name_to_find:
            return f"найдено!'{name_to_find}' есть в списке."
        current = current.next
    return f"увы, '{name_to_find}' не нашли."

node1 = Node("понедельник")
node2 = Node("вторник")
node3 = Node("среда")

node1.next = node2
node2.next = node3

head = node1
print_list(head)

node4 = Node("четверг")
add_node(head, node4)
print_list(head)

Результат = find_node(head, "вторник")
print(Результат)

head = delete_node(head, "вторник")
print_list(head)

head = delete_node(head, "понедельник")
print_list(head)

КОЛИЧЕСТВО = 10000

head_test = Node("старт")

start_time = time.time()
for i in range(КОЛИЧЕСТВО):
    new_node = Node(f"элемент_{i}")
    add_node(head_test, new_node)
end_time = time.time()

linked_list_time = end_time - start_time
print(f"связный список{КОЛИЧЕСТВО} элементов за: {linked_list_time:.4f} сек")

py_list = []

start_time = time.time()
for i in range(КОЛИЧЕСТВО):
    py_list.append(f"элемент_{i}")
end_time = time.time()

py_list_time = end_time - start_time
print(f"обычный список Python справился за: {py_list_time:.4f} сек")

разница = linked_list_time / py_list_time
print(f"\nРЕЗУЛЬТАТ: встроенный список Python оказался быстрее в {разница:.1f} раз!")
