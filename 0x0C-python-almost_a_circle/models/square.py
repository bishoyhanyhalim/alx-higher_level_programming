#!/usr/bin/python3
"""this is a square class for project"""

from models.rectangle import Rectangle
# from rectangle import Rectangle


class Square(Rectangle):
    """this is a square class for project"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, new_value):
        self.width = new_value
        self.height = new_value

    def __str__(self):
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def __update(self, id=None, size=None, x=None, y=None):
        """privet func method"""
        if id is not None:
            self.id = id
        if size is not None:
            self.size = size
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

    def update(self, *args, **kwargs):
        """this public func args and kwargs"""
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

    def to_dictionary(self):
        """now let's returns square to dict"""

        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
