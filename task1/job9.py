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

    def pre_order(self):
        if self.node_type == "club":
            s = self.stats
            print(f"- {self.name} (игр: {s['game']}, В: {s['win']}, Н: {s['draw']}, П: {s['lose']})")
        else:
            print(f"- {self.name} [{self.node_type.upper()}]")

        for child in self.children:
            child.pre_order()

    def post_order(self):
        for child in self.children:
            child.post_order()

        if self.node_type == "club":
            s = self.stats
            print(f"- {self.name} (игр: {s['game']}, В: {s['win']}, Н: {s['draw']}, П: {s['lose']})")
        else:
            print(f"- {self.name} [{self.node_type.upper()}]")

    def in_order(self):
        if self.children:
            self.children[0].in_order()

            if self.node_type == "club":
                s = self.stats
                print(f"- {self.name} (игр: {s['game']}, В: {s['win']}, Н: {s['draw']}, П: {s['lose']})")
            else:
                print(f"- {self.name} [{self.node_type.upper()}]")

            for child in self.children[1:]:
                child.in_order()
        else:
            if self.node_type == "club":
                s = self.stats
                print(f"- {self.name} (игр: {s['game']}, В: {s['win']}, Н: {s['draw']}, П: {s['lose']})")
            else:
                print(f"- {self.name} [{self.node_type.upper()}]")


root = Node("UEFA Champions League 2025", "root")

england = Node("England", "country")
spain = Node("Spain", "country")
germany = Node("Germany", "country")
italy = Node("Italy", "country")
france = Node("France", "country")
portugal = Node("Portugal", "country")
austria = Node("Austria", "country")

root.children = [england, spain, germany, italy, france, portugal, austria]

england.children = [
    Node("Chelsea", "club", {"game": 3, "win": 2, "draw": 0, "lose": 1}),
    Node("Manchester City", "club", {"game": 3, "win": 3, "draw": 0, "lose": 0})
]
spain.children = [
    Node("Real Madrid", "club", {"game": 3, "win": 2, "draw": 1, "lose": 0}),
    Node("Atlético Madrid", "club", {"game": 3, "win": 2, "draw": 0, "lose": 1})
]
germany.children = [
    Node("Bayern Munich", "club", {"game": 3, "win": 2, "draw": 0, "lose": 1}),
    Node("Borussia Dortmund", "club", {"game": 3, "win": 2, "draw": 1, "lose": 0})
]
italy.children = [
    Node("Inter Milan", "club", {"game": 3, "win": 2, "draw": 1, "lose": 0}),
    Node("Juventus", "club", {"game": 3, "win": 2, "draw": 0, "lose": 1})
]
france.children = [
    Node("Paris Saint-Germain", "club", {"game": 3, "win": 2, "draw": 0, "lose": 1})
]
portugal.children = [
    Node("Porto", "club", {"game": 3, "win": 0, "draw": 2, "lose": 1}),
    Node("Benfica", "club", {"game": 3, "win": 2, "draw": 1, "lose": 0})
]
austria.children = [
    Node("Red Bull Salzburg", "club", {"game": 3, "win": 1, "draw": 1, "lose": 1})
]


choice = input("хочешь добавить клуб? (да/нет): ").strip().lower()

if choice == "да":
    new_country = input("укажи страну: ").strip()
    new_club = input("укажи название команды: ").strip()
    print("\nотлично, теперь счет.")
    new_Team_Statistics = input("вот пример: 3 2 0 1 (всего игр, победы, ничьи, поражения):\n")

    g, w, d, l = map(int, new_Team_Statistics.split())
    stats_dict = {"game": g, "win": w, "draw": d, "lose": l}

    target_country_node = root.find_node(new_country)
    if not target_country_node:
        target_country_node = Node(new_country, "country")
        root.add_child(target_country_node)

    target_country_node.add_child(Node(new_club, "club", stats_dict))
    print(f"Клуб {new_club} успешно добавлен в страну {new_country}!\n")

elif choice == "нет":
    print("ой, ну и не надо((")
    sys.exit()

target_country = input("\nкакую страну ищем, Boss? ").strip()
country_node = root.find_node(target_country)

if country_node and country_node.node_type == "country":
    print(f"\nстрана '{country_node.name}' найдена.")
    print("выбери порядок обхода:\n1. Pre-order\n2. Post-order\n3. In-order")
    choice = input("укажи цифру: ").strip()

    print("\nнашел:")
    if choice == "1":
        country_node.pre_order()
    elif choice == "2":
        country_node.post_order()
    elif choice == "3":
        country_node.in_order()
    else:
        print("Неверная цифра обхода!")
        sys.exit()
else:
    print(f"извини, Boss, страна '{target_country}' не найдена в дереве.")
    sys.exit()
