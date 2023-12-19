#!/usr/bin/env python3
# lib/debug.py


from models.__init__ import CONN, CURSOR
from models.parent import Parent
from models.children import Children
import ipdb

def reset_database():
    Children.drop_table()
    Parent.drop_table()
    Parent.create_table()
    Children.create_table()

    shereen = Parent.create("sheshe", 25)
    kanny = Parent.create(
        "koko", 24)
    Children.create("Bano", "boy", shereen.id)
    Children.create("Shayar", "girl", shereen.id)
    Children.create("Yasir", "boy", kanny.id)
    Children.create("Deya", "girl", kanny.id)
 
reset_database()
ipdb.set_trace()

