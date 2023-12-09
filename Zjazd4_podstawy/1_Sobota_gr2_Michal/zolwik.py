"""
Zaimplementuj klasę Turtle
atrybuty: x, y, direction
metody:
def forward
def backward
def left
def right
Początkowy stan:
self.x = 0
self.y = 0
self.direction = "up"
"""
from typing import Literal, Union
from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class Animal:
    def forward(self, amount: int):
        ...

    def backward(self, amount: int):
        ...

    def left(self):
        ...

    def right(self):
        ...


class Turtle:

    def __init__(self, x: int = 0, y: int = 0, direction: Literal[0, 1, 2, 3] = 0):
        self.x = x
        self.y = y
        self.direction = direction

    # direction == 0 -> up
    # direction == 1 -> down
    # direction == 2 -> left
    # direction == 3 -> right

    def forward(self, amount: int) -> tuple[int, int]:
        offsets = {
            0: (0, 1),
            1: (0, -1),
            2: (-1, 0),
            3: (1, 0)
        }
        self.x += amount * offsets[self.direction][0]
        self.y += amount * offsets[self.direction][1]
        return self.x, self.y

    def right(self) -> int:
        if self.direction == 0:
            self.direction = 3
        elif self.direction == 1:
            self.direction = 2
        elif self.direction == 2:
            self.direction = 0
        elif self.direction == 3:
            self.direction = 1
        return self.direction

    def backward(self, amount: int) -> tuple[int, int]:
        if self.direction == 0:
            self.y -= amount
        elif self.direction == 1:
            self.y += amount
        elif self.direction == 2:
            self.x += amount
        elif self.direction == 3:
            self.x -= amount
        return self.x, self.y

    def left(self) -> int:
        if self.direction == 0:
            self.direction = 2
        elif self.direction == 1:
            self.direction = 3
        elif self.direction == 2:
            self.direction = 1
        elif self.direction == 3:
            self.direction = 0
        return self.direction


class Ant:

    def __init__(self, x: int = 0, y: int = 0):
        self.x = x
        self.y = y

    def forward(self, amount: int) -> tuple[int, int]:
        self.y += amount
        return self.x, self.y

    def right(self, amount: int = 1) -> tuple[int, int]:
        self.x += amount
        return self.x, self.y

    def backward(self, amount: int) -> tuple[int, int]:
        self.y -= amount
        return self.x, self.y

    def left(self, amount: int = 1) -> tuple[int, int]:
        self.x -= amount
        return self.x, self.y


def my_custom_animal_path(animal):
    points = [(0, 0)]
    points.append(animal.forward(3))
    animal.right()
    points.append(animal.forward(2))
    animal.right()
    points.append(animal.backward(1))

    plt.scatter(*zip(*points))
    plt.plot(*zip(*points))
    plt.show()


my_custom_animal_path(Turtle())
my_custom_animal_path(Ant())
my_custom_animal_path(56)
