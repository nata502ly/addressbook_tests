import json
from models.group import Group
import os.path

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "groups.json")

with open(file_name, encoding='utf8') as f:
    groups_list = [Group(**data) for data in json.load(f)]

# groups_list = []
# for data in groups_data:
#     g = Group(name=data["name"], header=data["header"], footer=data["footer"])
#     groups_list.append(g)

if __name__ == "__main__":
    print(groups_list)
