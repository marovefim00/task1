import sys


class Node:
    def __init__(self, name, node_type="root", stats=None):
        self.name = name
        self.node_type = node_type
        self.stats = stats
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def find_node(self, target_name):
        if self.name.lower() == target_name.lower():
            return self
        for child in self.children:
            found = child.find_node(target_name)
            if found:
                return found
        return None

    def remove_child(self, target_name):
        for child in self.children:
            if child.name.lower() == target_name.lower():
                self.children.remove(child)
                return True
            if child.remove_child(target_name):
                return True
        return False

    def print_tree(self, level=0):
        indent = "  " * level
        if self.node_type == "club":
            s = self.stats
            print(f"{indent} {self.name} (игр: {s['game']}, в: {s['win']}, н: {s['draw']}, п: {s['lose']})")
        elif self.node_type == "country":
            print(f"{indent} {self.name} [{self.node_type.upper()}]")
        else:
            print(f"{indent} {self.name} [{self.node_type.upper()}]")

        for child in self.children:
            child.print_tree(level + 1)

    def pre_order(self):
        if self.node_type == "club":
            s = self.stats
            print(f"- {self.name} (игр: {s['game']}, в: {s['win']}, н: {s['draw']}, п: {s['lose']})")
        else:
            print(f"- {self.name} [{self.node_type.upper()}]")
        for child in self.children:
            child.pre_order()

    def post_order(self):
        for child in self.children:
            child.post_order()
        if self.node_type == "club":
            s = self.stats
            print(f"- {self.name} (игр: {s['game']}, в: {s['win']}, н: {s['draw']}, п: {s['lose']})")
        else:
            print(f"- {self.name} [{self.node_type.upper()}]")

    def in_order(self):
        if self.children:
            self.children.in_order()
            if self.node_type == "club":
                s = self.stats
                print(f"- {self.name} (игр: {s['game']}, в: {s['win']}, н: {s['draw']}, п: {s['lose']})")
            else:
                print(f"- {self.name} [{self.node_type.upper()}]")
            for child in self.children[1:]:
                child.in_order()
        else:
            if self.node_type == "club":
                s = self.stats
                print(f"- {self.name} (игр: {s['game']}, в: {s['win']}, н: {s['draw']}, п: {s['lose']})")
            else:
                print(f"- {self.name} [{self.node_type.upper()}]")


root = Node("uefa champions league 2025", "root")
england = Node("england", "country")
spain = Node("spain", "country")
germany = Node("germany", "country")
italy = Node("italy", "country")
france = Node("france", "country")
portugal = Node("portugal", "country")
austria = Node("austria", "country")

root.children = [england, spain, germany, italy, france, portugal, austria]
england.children = [
    Node("chelsea", "club", {"game": 3, "win": 2, "draw": 0, "lose": 1}),
    Node("manchester city", "club", {"game": 3, "win": 3, "draw": 0, "lose": 0})
]
spain.children = [
    Node("real madrid", "club", {"game": 3, "win": 2, "draw": 1, "lose": 0}),
    Node("atlético madrid", "club", {"game": 3, "win": 2, "draw": 0, "lose": 1})
]
germany.children = [
    Node("bayern munich", "club", {"game": 3, "win": 2, "draw": 0, "lose": 1}),
    Node("borussia dortmund", "club", {"game": 3, "win": 2, "draw": 1, "lose": 0})
]
italy.children = [
    Node("inter milan", "club", {"game": 3, "win": 2, "draw": 1, "lose": 0}),
    Node("juventus", "club", {"game": 3, "win": 2, "draw": 0, "lose": 1})
]
france.children = [
    Node("paris saint-germain", "club", {"game": 3, "win": 2, "draw": 0, "lose": 1})
]
portugal.children = [
    Node("porto", "club", {"game": 3, "win": 0, "draw": 2, "lose": 1}),
    Node("benfica", "club", {"game": 3, "win": 2, "draw": 1, "lose": 0})
]
austria.children = [
    Node("red bull salzburg", "club", {"game": 3, "win": 1, "draw": 1, "lose": 1})
]

choice = input("хочешь добавить клуб? (да/нет): ").strip().lower()
if choice == "да":
    new_country = input("укажи страну: ").strip()
    new_club = input("укажи название команды: ").strip()
    print("\nотлично, теперь счет.")
    new_team_statistics = input("вот пример: 3 2 0 1 (всего игр, победы, ничьи, поражения):\n")
    g, w, d, l = map(int, new_team_statistics.split())
    stats_dict = {"game": g, "win": w, "draw": d, "lose": l}

    target_country_node = root.find_node(new_country)
    if not target_country_node:
        target_country_node = Node(new_country, "country")
        root.add_child(target_country_node)

    target_country_node.add_child(Node(new_club, "club", stats_dict))
    print(f"клуб {new_club} успешно добавлен в страну {new_country}!\n")
elif choice == "нет":
    print("хорошо, идем дальше.\n")

while True:
    print("\nглавное меню")
    print("1. посмотреть всё дерево целиком")
    print("2. обход конкретной страны (pre/post/in-order)")
    print("3. удалить элемент (страну или клуб)")
    print("4. выйти")

    main_choice = input("выбери действие (1-4): ").strip()

    if main_choice == "1":
        print("\nструктура всего дерева")
        root.print_tree()

    elif main_choice == "2":
        target_country = input("\nкакую страну ищем, boss? ").strip()
        country_node = root.find_node(target_country)

        if country_node and country_node.node_type == "country":
            print(f"\nстрана '{country_node.name}' найдена.")
            print("выбери порядок обхода:\n1. pre-order\n2. post-order\n3. in-order")
            traverse_choice = input("укажи цифру: ").strip()
            print("\nнашел:")
            if traverse_choice == "1":
                country_node.pre_order()
            elif traverse_choice == "2":
                country_node.post_order()
            elif traverse_choice == "3":
                country_node.in_order()
            else:
                print("неверная цифра обхода!")
        else:
            print(f"извини, boss, страна '{target_country}' не найдена в дереве.")

    elif main_choice == "3":
        delete_target = input("\nчто удалить (название страны или клуба)? ").strip()
        was_deleted = root.remove_child(delete_target)
        if was_deleted:
            print(f"успешно удалено: '{delete_target}'")
        else:
            print(f"элемент '{delete_target}' не найден в дереве.")

    elif main_choice == "4":
        print("пока, boss!")
        sys.exit()
    else:
        print("неверный пункт меню!")
