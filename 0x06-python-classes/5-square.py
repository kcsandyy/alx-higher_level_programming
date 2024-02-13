#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if self.__validate_size(size):
            self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if self.__validate_size(value):
            self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        i = 0
        for i in range(0, self.__size):
            j = 0
            for j in range(0, self.__size):
                print("#", end='')
            print()

    def __validate_size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            return True
        return False
