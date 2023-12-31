from models.parent import Parent
from models.children import Children
from models.__init__ import CURSOR


def exit_program():
    print(" ")
    print("See you next time!")
    exit()


def list_parents():
    parents = Parent.get_all()
    # for parent in parents:
    print(" ")
    for i, parent in enumerate(parents, start=1):
        # ...    print(i, value)
        print(f'{i}. Parent name is: {parent.name} and age: {parent.age}\n')
    print(" ")


def find_parent_by_name():
    print(" ")
    name = input("Enter the parent's name: ")
    parent = Parent.find_by_name(name)
    if parent:
        print(" ")
        print(f'Parent name is: {parent.name} and age: {parent.age}')
        print(" ")
    else:
        print(" ")
        print(f'Parent {name} not found')
        print(" ")


def find_parent_by_age():
    print(" ")
    age = input("Enter the parent's age: ")
    parent = Parent.find_by_age(age)
    if parent:
        print(" ")
        print(f"\nAge {parent.age} for the parent's name: {parent.name}\n")
        print(" ")
    else:
        print(" ")
        print(f'Parent with age: {age} not found')
        print(" ")


def create_parent():
    print(" ")
    name = input("Enter the parent's name: ")
    while True:
        print(" ")
        age_input = input("Enter the parent's age: ")
        try:
            age = int(age_input)
            break
        except ValueError:
            print("Please enter a valid age.")

    try:
        parent = Parent.create(name, age)
        print(" ")
        print(
            f'New parent: {parent.name} has been created and the age is: {parent.age}')
        print(" ")
        return parent
    except Exception as exc:
        print("Error creating parent: ", exc)
        return None


def delete_parent():
    print(" ")
    name = input("Enter the parent's name: ")
    if parent := Parent.find_by_name(name):
        parent.delete()
        print(" ")
        print(f'parent {name} deleted')
        print(" ")
    else:
        print(" ")
        print(f'parent {name} not found')
        print(" ")


def list_childrens():
    childrens = Children.get_all()
    print(" ")
    for i, children in enumerate(childrens, start=1):
        # ...    print(i, value)
        print(f'{i}. Child name is: {children.name} and gender: {children.gender}\n')
    print(" ")


def find_children_by_name():
    print(" ")
    name = input("Enter the children's name: ")
    children = Children.find_by_name(name)
    if children:
        print(" ")
        print(
            f'Child name is: {children.name} and gender is: {children.gender}')
        print(" ")
    else:
        print(" ")
        print(f'Child {name} not found')
        print(" ")


def find_children_by_gender():
    print(" ")
    gender = input("Enter the children's gender: ")
    children = Children.find_by_gender(gender)
    if children:
        print(" ")
        print(
            f"\n {children.gender} is the gender for the Child's name: {children.name}\n")
        print(" ")
    else:
        print(" ")
        print(f'Child with age: {gender} not found')
        print(" ")


def find_parent_id_by_name(parent_name):
    sql = """
        SELECT id
        FROM parents
        WHERE name = ?
    """
    row = CURSOR.execute(sql, (parent_name,)).fetchone()
    return row[0] if row else None

def create_children():
    name = input("Enter the children's name: ")
    gender = input("Enter the children's gender: ")

    parent_id = None
    while parent_id is None:
        parent_name_input = input("Enter the children's parent's name: ")
        parent_id = find_parent_id_by_name(parent_name_input)
        if parent_id is None:
            print("Parent not found. Please enter a valid parent's name.")

    try:
        children = Children.create(name, gender, parent_id)
        print(f"\nChild {name} with gender {gender} has been added.\n")
        return children
    except Exception as exc:
        print("Error creating child: ", exc)
        return None


def delete_children():
    name = input("Enter the child's name: ")
    if children := Children.find_by_name(name):
        children.delete()
        print(f'Child {name} is deleted')
    else:
        print(f'children {name} not found')


def list_parent_childrens():
    print(" ")
    name = input("Enter the parent's name: ")
    parent = Parent.find_by_name(name)
    if parent:
        children_list = parent.children()
        if children_list:
            for child in children_list:
                print(" ")
                print(
                    f'Child {child.name} and the gender is {child.name} for the parent: {parent.name}')
                print(" ")
        else:
            print(f'No children found for parent {name}')
    else:
        print(f'Parent {name} not found')
