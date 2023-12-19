from models.parents import Parent
from models.children import Children


def exit_program():
    print("Goodbye!")
    exit()


def list_parents():
    parents = Parent.get_all()
    for parent in parents:
        print(parent)


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
    location = input("Enter the parent's location: ")
    try:
        parent = Parent.create(name, location)
        print(f'Success: {parent}')
    except Exception as exc:
        print("Error creating parent: ", exc)


def update_parent():
    id_ = input("Enter the parent's id: ")
    if parent := Parent.find_by_id(id_):
        try:
            name = input("Enter the parent's new name: ")
            parent.name = name
            location = input("Enter the parent's new location: ")
            parent.location = location

            parent.update()
            print(f'Success: {parent}')
        except Exception as exc:
            print("Error updating parent: ", exc)
    else:
        print(f'parent {id_} not found')


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
    job_title = input("Enter the children's job title: ")
    parent_id = input("Enter the children's parent ID: ")

    try:
        children = Children.create(name, job_title, parent_id)
        print(f'Success: {children}')
    except ValueError:
        print("Invalid parent ID. Please enter a valid number.")
    except Exception as exc:
        print("Error creating children: ", exc)



def update_children():
    id_ = input("Enter the children's id: ")
    if children := Children.find_by_id(id_):
        try:
            name = input("Enter the children's new name: ")
            children.name = name
            job_title = input("Enter the children's new job_title: ")
            children.job_title = job_title
            parent_id = input("Enter the children's new parent_id: ")
            children.parent_id = parent_id

            children.update()
            print(f'Success: {children}')
        except Exception as exc:
            print("Error updating children: ", exc)
    else:
        print(f'children {id_} not found')


def delete_children():
    id_ = input("Enter the children's id: ")
    if children := Children.find_by_id(id_):
        children.delete()
        print(f'children {id_} deleted')
    else:
        print(f'children {id_} not found')


def list_parent_childrens():
    
    parent_id = input("Enter the parent's id: ")

    childrens = Children.find_by_id_all(parent_id)
    print(childrens) if childrens else print(f'No childrens found in parent {parent_id}')

