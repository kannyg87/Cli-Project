from models.parent import Parent
from models.children import Children


def exit_program():
    print("See you next time!")
    exit()


def list_parents():
    parents = Parent.get_all()
    # for parent in parents:
    print(" ")
    for i, parent in enumerate(parents, start=1):
        # ...    print(i, value)
        print(f'{i}. Parent name is: {parent.name} and age: {parent.age}')
    print(" ")

def find_parent_by_name():
    name = input("Enter the parent's name: ")
    parent = Parent.find_by_name(name)
    print(parent) if parent else print(
        f'parent {name} not found')


def find_parent_by_id():
    id_ = input("Enter the parent's id: ")
    parent = Parent.find_by_id(id_)
    print(parent) if parent else print(f'parent {id_} not found')


def create_parent():
    name = input("Enter the parent's name: ")
    while True:
        age_input = input("Enter the parent's age: ")
        try:
            age = int(age_input)
            break
        except ValueError:
            print("Please enter a valid age.")

    try:
        parent = Parent.create(name, age)
        print(f'Success: {parent}')
        return parent
    except Exception as exc:
        print("Error creating parent: ", exc)
        return None


def delete_parent():
    id_ = input("Enter the parent's id: ")
    if parent := Parent.find_by_id(id_):
        parent.delete()
        print(f'parent {id_} deleted')
    else:
        print(f'parent {id_} not found')


def list_childrens():
    childrens = Children.get_all()
    for children in childrens:
        print(children)


def find_children_by_name():
    name = input("Enter the children's name: ")
    children = Children.find_by_name(name)
    print(children) if children else print(
        f'Empolyee {name} not found')


def find_children_by_id():
    id_ = input("Enter the children's id: ")
    children = Children.find_by_id(id_)
    print(children) if children else print(f'children {id_} not found')


def create_children():
    name = input("Enter the children's name: ")
    gender = input("Enter the children's gender: ")

    while True:
        parent_id_input = input("Enter the children's parent ID: ")
        try:
            parent_id = int(parent_id_input)
            break
        except ValueError:
            print("Invalid parent ID. Please enter a valid number.")

    try:
        children = Children.create(name, gender, parent_id)
        print(f'Success: {children}')
        return children
    except Exception as exc:
        print("Error creating children: ", exc)
        return None


def delete_children():
    id_ = input("Enter the children's id: ")
    if children := Children.find_by_id(id_):
        children.delete()
        print(f'children {id_} deleted')
    else:
        print(f'children {id_} not found')


def list_parent_childrens():

    name = input("Enter the parent's name: ")
    parent = Parent.find_by_name(name)
    childrens = parent.children()
    # childrens = Children.find_by_id_all(name)
    breakpoint
    print(childrens) if childrens else print(
        f'No childrens found in parent {name}')
