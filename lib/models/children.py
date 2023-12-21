# lib/models/children.py
from models.__init__ import CURSOR, CONN
from models.parent import Parent


class Children:

    all = {}

    def __init__(self, name, gender, parent_id, id=None):
        self.id = id
        self.name = name
        self.gender = gender
        self.parent_id = parent_id

    # def __repr__(self):
    #     return (
    #         f"<Children {self.id}: {self.name}, {self.gender}, " +
    #         f"Parent ID: {self.parent_id}>"
    #     )

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
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if isinstance(gender, str) and len(gender):
            self._gender = gender
        else:
            raise ValueError(
                "gender must be a non-empty string"
            )

    @property
    def parent_id(self):
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        if type(parent_id) is not int:
            raise ValueError("parent_id must be an integer")
        self._parent_id = parent_id

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of children instances """
        sql = """
            CREATE TABLE IF NOT EXISTS children (
            id INTEGER PRIMARY KEY,
            name TEXT,
            gender TEXT,
            parent_id INTEGER,
            FOREIGN KEY (parent_id) REFERENCES parents(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists children instances """
        sql = """
            DROP TABLE IF EXISTS children;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the name, job title, and parent id values of the current children object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO children (name, gender, parent_id)
                VALUES (?, ?, ?)
        """

        CURSOR.execute(sql, (self.name, self.gender, self.parent_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current children instance."""
        sql = """
            UPDATE children
            SET name = ?, gender = ?, parent_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.gender,
                             self.parent_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current children instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM children
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, name, gender, parent_id):
        """ Initialize a new children instance and save the object to the database """
        children = cls(name, gender, parent_id)
        children.save()
        return children

    @classmethod
    def instance_from_db(cls, row):
        """Return an children object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        children = cls.all.get(row[0])
        if children:
            # ensure attributes match row values in case local instance was modified
            children.name = row[1]
            children.gender = row[2]
            children.parent_id = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            children = cls(row[1], row[2], row[3])
            children.id = row[0]
            cls.all[children.id] = children
        return children

    @classmethod
    def get_all(cls):
        """Return a list containing one children object per table row"""
        sql = """
            SELECT *
            FROM children
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_name(cls, name):
        """Return children object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM children
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_gender(cls, gender):
        """Return children object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM children
            WHERE gender = ?
        """

        row = CURSOR.execute(sql, (gender,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_id(cls, id):
        """Return children object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM children
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def find_by_id_all(cls, id):
        sql = """
            SELECT *
            FROM children
            WHERE parent_id = ?
        """
        rows = CURSOR.execute(sql, (id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows] if rows else None