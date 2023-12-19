#!/usr/bin/env python3
# lib/debug.py


from models.__init__ import CONN, CURSOR
from models.parents import Parent
from models.children import Children
import ipdb

def reset_database():
    Children.drop_table()
    Parent.drop_table()
    Parent.create_table()
    Children.create_table()

    shereen = Parent.create("Ali", "25")
    kanny = Parent.create(
        "Human Resources", "Building C, East Wing")
    Children.create("Bano", "boy", shereen.id)
    Children.create("Shayar", "girl", shereen.id)
    Children.create("Yasir", "girl", kanny.id)
    Children.create("Deya", "boy", kanny.id)
 
reset_database()
ipdb.set_trace()

