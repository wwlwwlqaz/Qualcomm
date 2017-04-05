import os

global capacity_list
capacity_list = []

def get_capacity_list():
    file_name_list = os.listdir("./capacity/");
    for file_name in file_name_list:
        if file_name != "capacity.py" and file_name != "__init__.py" and file_name.endswith(".py"):
            module = __import__(file_name[:-3], globals(), locals(), [], -1)
            capacity = module.query_capacity()
            if capacity != None:
                capacity_list.append(capacity)