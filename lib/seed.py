#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.parents import Parent
from models.children import Children

def seed_database():
    Children.drop_table()
    Parent.drop_table()
    Parent.create_table()
    Children.create_table()

    # Create seed data
    shereen = Parent.create("Ali", "25")
    kanny = Parent.create(
        "Human Resources", "Building C, East Wing")
    Children.create("Bano", "boy", shereen.id)
    Children.create("Shayar", "girl", shereen.id)
    Children.create("Yasir", "girl", kanny.id)
    Children.create("Deya", "boy", kanny.id)


seed_database()
print("Seeded database")
