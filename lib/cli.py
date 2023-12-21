from helpers import (
    exit_program,
    list_parents,
    find_parent_by_name,
    find_parent_by_age,
    create_parent,
    delete_parent,
    list_childrens,
    find_children_by_name,
    find_children_by_gender,
    create_children,
    delete_children,
    list_parent_childrens
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_parents()
        elif choice == "2":
            find_parent_by_name()
        elif choice == "3":
            find_parent_by_age()
        elif choice == "4":
            create_parent()
        elif choice == "5":
            delete_parent()
        elif choice == "6":
            list_childrens()
        elif choice == "7":
            find_children_by_name()
        elif choice == "8":
            find_children_by_gender()
        elif choice == "9":
            create_children()
        elif choice == "10":
            delete_children()
        elif choice == "11":
            list_parent_childrens()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all parents")
    print("2. Find parent by name")
    print("3. Find parent by age")
    print("4: Create parent")
    print("5: Delete parent")
    print("6. List all childrens")
    print("7. Find children by name")
    print("8. Find children by gender")
    print("9: Create children")
    print("10: Delete children")
    print("11: List all childrens in a parent")


if __name__ == "__main__":
    main()
