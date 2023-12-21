# lib/models/parent.py
from models.__init__ import CURSOR, CONN



class Parent:

    all = {}

    def __init__(self, name, age, id=None):
        self.id = id
        self.name = name
        self.age = age

    # def __repr__(self):
    #     return f"<Parent {self.id}: {self.name}, {self.age}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError(
                "Name must be a non-empty string"
            )

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int) and age > 18:
            self._age = age
        else:
            raise ValueError(
                "age must be greater than integer"
            )

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of parent instances """
        sql = """
            CREATE TABLE IF NOT EXISTS parents (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists parent instances """
        sql = """
            DROP TABLE IF EXISTS parents;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name and age values of the current parent instance.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
            INSERT INTO parents (name, age)
            VALUES (?, ?)
        """

        CURSOR.execute(sql, (self.name, self.age))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, age):
        """ Initialize a new parent instance and save the object to the database """
        parent = cls(name, age)
        parent.save()
        return parent

    def update(self):
        """Update the table row corresponding to the current parent instance."""
        sql = """
            UPDATE parents
            SET name = ?, age = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.age, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current parent instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM parents
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a parent object having the attribute values from the table row."""

        # Check the dictionary for an existing instance using the row's primary key
        parent = cls.all.get(row[0])
        if parent:
            # ensure attributes match row values in case local instance was modified
            parent.name = row[1]
            parent.age = row[2]
        else:
            # not in dictionary, create new instance and add to dictionary
            parent = cls(row[1], row[2])
            parent.id = row[0]
            cls.all[parent.id] = parent
        return parent

    @classmethod
    def get_all(cls):
        """Return a list containing a parent object per row in the table"""
        sql = """
            SELECT *
            FROM parents
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a parent object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM parents
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        """Return a parent object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM parents
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def parents(self):
        """Return list of parent associated with current parent"""
        from lib.models.parent import Parent
        sql = """
            SELECT * FROM parent
            WHERE parent_id = ?
        """
        CURSOR.execute(sql, (self.id,),)

        rows = CURSOR.fetchall()
        return [
            Parent.instance_from_db(row) for row in rows
        ]
    
    def children(self):
        from models.children import Children
        childrens = Children.find_by_id_all(self.id)
        breakpoint()
        