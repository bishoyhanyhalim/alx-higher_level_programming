#!/usr/bin/python3
"""this is a rectangle class for project"""

from models.base import Base


class Rectangle(Base):

    """this is a rectangle class for project"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """this is a defined func

        Args:
            this is variable of ths class
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """set and get width"""
        return self.__width

    @width.setter
    def width(self, new_value):
        if type(new_value) is not int:
            raise TypeError("width must be an integer")
        if new_value <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_value

    @property
    def height(self):
        """set and get height"""
        return self.__height

    @height.setter
    def height(self, new_value):
        if type(new_value) is not int:
            raise TypeError("height must be an integer")
        if new_value <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_value

    @property
    def x(self):
        """set and get x"""
        return self.__x

    @x.setter
    def x(self, new_value):
        if type(new_value) is not int:
            raise TypeError("x must be an integer")
        if new_value < 0:
            raise ValueError("x must be >= 0")
        self.__x = new_value

    @property
    def y(self):
        """set and get y"""
        return self.__y

    @y.setter
    def y(self, new_value):
        if type(new_value) is not int:
            raise TypeError("y must be an integer")
        if new_value < 0:
            raise ValueError("y must be >= 0")
        self.__y = new_value

    def area(self):
        """now let's get the area of rectangle"""
        return self.width * self.height

    def display(self):
        """some magic to print custom #"""

        for num in range(self.y):
            print(self.x * "")
        for num in range(self.height):
            print(self.x * " ", end="")
            print(self.width * "#")

    def __str__(self):
        """this func can print [Rectangle] (<id>) <x>/<y> - <width>/<height>"""
        return (
            f"[Rectangle] ({self.id}) "
            f"{self.x}/{self.y} - {self.width}/{self.height}"
        )

    # def update(self, *args):
    #     """this new update"""
    #     attrs = ["id", "width", "height", "x", "y"]
    #     for num in range(len(args)):
    #         setattr(self, attrs[num], args[num])

    def update(self, *args, **kwargs):
        """this new update"""
        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
