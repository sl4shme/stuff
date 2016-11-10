"""
  0 1 2 3 4 5 6 7
0 * * * * * * * *
1 * * * * * * * *
2 * * * * * * * *
3 * * * X * * * *
4 * * * X * * * *
5 * * * X * * * *
6 * * * * * * * *
7 * * * * * * * *

Given a grid of size n*n that contains one 3 cell ship, create a function that
outputs the position of the ship like ((3,3), (3,4) ,(3,5))

You are given a matrix object with a bomb method: bomb(x,y) that return True
if a ship was bombed and False if missed.

The goal is to call bomb() as less as possible.
"""
import random


def generate_ship(size):
    """
    Generates a random ship in a n*n grid for testing
    """
    n = size - 1
    x = random.randint(0, n)
    y = random.randint(0, n)
    direction = random.choice(["ver", "hor"])
    if direction == "ver":
        ship = [(x, y), (x + 1, y), (x + 2, y)]
    else:
        ship = [(x, y), (x, y + 1), (x, y + 2)]
    for i in ship:
        if i[0] > n or i[1] > n:
            ship = generate_ship(size)
            break
    return ship


class Matrix():
    """
    Matrix class for testing
    """
    def __init__(self, n):
        self.n = n
        self.ship = generate_ship(n)
        self.tries = 0

    def bomb(self, x, y):
        """
        Tries to bomb the ship
        """
        self.tries += 1
        if (x, y) in self.ship:
            return True
        else:
            return False


def find_ship(matrix):
    """
    Dumb bruteforce
    """
    res = []
    for x in range(matrix.n):
        for y in range(matrix.n):
            if matrix.bomb(x, y):
                res.append((x, y))
    return res[0], res[1], res[2]


av = []
for i in range(1000):
    m = Matrix(10)
    r = find_ship(m)
    av.append(m.tries)
print("find_ship average: {} tries".format(sum(av) / len(av)))


def find_ship_2(matrix):
    """
    Dumb bruteforce but stops when found
    """
    res = []
    for x in range(matrix.n):
        for y in range(matrix.n):
            if matrix.bomb(x, y):
                res.append((x, y))
                if len(res) == 3:
                    return res[0], res[1], res[2]

av = []
for i in range(1000):
    m = Matrix(10)
    r = find_ship_2(m)
    av.append(m.tries)
print("find_ship_2 average: {} tries".format(sum(av) / len(av)))


def _find_from_hit(x, y, matrix):
    """
    Find ship from a first hit
    Does not take border into account
    """
    res = [(x, y)]
    # Horizontal right
    if matrix.bomb(x + 1, y):
        res.append((x + 1, y))
        if matrix.bomb(x + 2, y):
            res.append((x + 2, y))
            return res
        else:
            # Horizontal center
            res.insert(0, (x - 1, y))
            return res
    elif matrix.bomb(x - 1, y):
        # Horizontal left
        res.insert(0, (x - 1, y))
        res.insert(0, (x - 2, y))
        return res
    # Vertical Down
    elif matrix.bomb(x, y + 1):
        res.append((x, y + 1))
        if matrix.bomb(x, y + 2):
            res.append((x, y + 2))
            return res
        else:
            # Vertical center
            res.insert(0, (x, y - 1))
            return res
    elif matrix.bomb(x, y - 1):
        # Vertical up
        res.insert(0, (x, y - 1))
        res.insert(0, (x, y - 2))
        return res


def find_ship_3(matrix):
    """
    Bruteforce until first position found
    """
    for x in range(matrix.n):
        for y in range(matrix.n):
            if matrix.bomb(x, y):
                return _find_from_hit(x, y, matrix)


av = []
for i in range(1000):
    m = Matrix(10)
    r = find_ship_3(m)
    av.append(m.tries)
print("find_ship_3 average: {} tries".format(sum(av) / len(av)))


def find_ship_4(matrix):
    """
    Random until first position found
    """
    tried = []
    while len(tried) <= (matrix.n * matrix.n):
        x = random.randint(0, matrix.n)
        y = random.randint(0, matrix.n)
        if (x, y) in tried:
            continue
        if _find_from_hit(x, y, matrix):
            return _find_from_hit(x, y, matrix)
        else:
            tried.append((x, y))


av = []
for i in range(1000):
    m = Matrix(10)
    r = find_ship_4(m)
    av.append(m.tries)
print("find_ship_4 average: {} tries".format(sum(av) / len(av)))


def find_ship_5(matrix):
    """
    We don't need to check every cell, only one out of three
      0 1 2 3 4 5 6 7
    0 x * * x * * x *
    1 * x * * x * * x
    2 * * x * * x * *
    3 x * * x * * x *
    4 * x * * x * * x
    5 * * x * * x * *
    6 x * * x * * x *
    7 * x * * x * * x
    """
    offset = 0
    for y in range(matrix.n):
        if offset == 0:
            for x in range(0, matrix.n, 3):
                if matrix.bomb(x, y):
                    return _find_from_hit(x, y, matrix)
            offset = 1
            continue
        if offset == 1:
            for x in range(1, matrix.n, 3):
                if matrix.bomb(x, y):
                    return _find_from_hit(x, y, matrix)
            offset = 2
            continue
        if offset == 2:
            for x in range(2, matrix.n, 3):
                if matrix.bomb(x, y):
                    return _find_from_hit(x, y, matrix)
            offset = 0

av = []
for i in range(1000):
    m = Matrix(10)
    r = find_ship_5(m)
    av.append(m.tries)
print("find_ship_5 average: {} tries".format(sum(av) / len(av)))
