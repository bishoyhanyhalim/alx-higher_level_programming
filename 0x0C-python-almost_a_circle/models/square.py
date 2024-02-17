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
