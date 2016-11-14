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
import sys


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


def run_test(f, matrixes):
    """
    Run c iterations of test with a matrix of n*n and display the average
    number of bomb needed to discover the ship
    """
    tries = []
    for m in matrixes:
        try:
            del m.cache
        except:
            pass
        m.tries = 0
        r = f(m)
        if r != (m.ship[0], m.ship[1], m.ship[2]):
            raise Exception("Wrong result with function: {}. Ship: {}. Result:"
                            "{}".format(f.__name__, m.ship, r))
        tries.append(m.tries)
        average = round(sum(tries) / len(tries), 3)
        max_tries = m.n * m.n
        percentage = round((average * 100) / max_tries, 3)
    print("Function {} averages: {} / {} tries or {} %".format(f.__name__,
                                                               average,
                                                               max_tries,
                                                               percentage))


def bruteforce(matrix):
    """
    Dumb bruteforce
    """
    res = []
    for x in range(matrix.n):
        for y in range(matrix.n):
            if matrix.bomb(x, y):
                res.append((x, y))
    return res[0], res[1], res[2]


def smart_bruteforce(matrix):
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
            return res[0], res[1], res[2]
        else:
            # Horizontal center
            res.insert(0, (x - 1, y))
            return res[0], res[1], res[2]
    elif matrix.bomb(x - 1, y):
        # Horizontal left
        res.insert(0, (x - 1, y))
        res.insert(0, (x - 2, y))
        return res[0], res[1], res[2]
    # Vertical Down
    elif matrix.bomb(x, y + 1):
        res.append((x, y + 1))
        if matrix.bomb(x, y + 2):
            res.append((x, y + 2))
            return res[0], res[1], res[2]
        else:
            # Vertical center
            res.insert(0, (x, y - 1))
            return res[0], res[1], res[2]
    elif matrix.bomb(x, y - 1):
        # Vertical up
        res.insert(0, (x, y - 1))
        res.insert(0, (x, y - 2))
        return res[0], res[1], res[2]


def bruteforce_until_hit(matrix):
    """
    Bruteforce until first position found
    """
    for x in range(matrix.n):
        for y in range(matrix.n):
            if matrix.bomb(x, y):
                return _find_from_hit(x, y, matrix)


def random_until_hit(matrix):
    """
    Random until first position found
    """
    # Generate a list of posible cells
    cells = [(x, y) for x in range(matrix.n) for y in range(matrix.n)]
    random.shuffle(cells)

    for cell in cells:
        if matrix.bomb(cell[0], cell[1]):
            return _find_from_hit(cell[0], cell[1], matrix)


def one_out_of_three_until_hit(matrix):
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


def _find_from_hit_border(x, y, matrix):
    """
    Find ship from a first hit
    Takes border into account
    The smaller the matrix is the bigger the difference it makes
    """
    s = matrix.n - 1
    res = [(x, y)]
    # Horizontal right
    if x != s and matrix.bomb(x + 1, y):
        res.append((x + 1, y))
        if x != (s - 1) and matrix.bomb(x + 2, y):
            res.append((x + 2, y))
            return res[0], res[1], res[2]
        else:
            # Horizontal center
            res.insert(0, (x - 1, y))
            return res[0], res[1], res[2]
    elif x != 0 and matrix.bomb(x - 1, y):
        # Horizontal left
        res.insert(0, (x - 1, y))
        res.insert(0, (x - 2, y))
        return res[0], res[1], res[2]
    # Vertical Down
    elif y != s and matrix.bomb(x, y + 1):
        res.append((x, y + 1))
        if y != (s - 1) and matrix.bomb(x, y + 2):
            res.append((x, y + 2))
            return res[0], res[1], res[2]
        else:
            # Vertical center
            res.insert(0, (x, y - 1))
            return res[0], res[1], res[2]
    elif y != 0 and matrix.bomb(x, y - 1):
        # Vertical up
        res.insert(0, (x, y - 1))
        res.insert(0, (x, y - 2))
        return res[0], res[1], res[2]


def bomb_with_cache(self, x, y):
    """
    Wraps the bomb() method in order to never bomb the same spot twice
    """
    try:
        return self.cache[(x, y)]
    except AttributeError:
        self.cache = {}
        return self.bomb(x, y)
    except KeyError:
        r = self._bomb(x, y)
        self.cache[(x, y)] = r
        return r


def one_out_of_three_until_hit_random(matrix):
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
    # Generate a list of posible cells
    cells = []
    offset = 0
    for y in range(matrix.n):
        if offset == 0:
            for x in range(0, matrix.n, 3):
                cells.append((x, y))
            offset = 1
            continue
        if offset == 1:
            for x in range(1, matrix.n, 3):
                cells.append((x, y))
            offset = 2
            continue
        if offset == 2:
            for x in range(2, matrix.n, 3):
                cells.append((x, y))
            offset = 0

    # Randomize the list
    random.shuffle(cells)

    for cell in cells:
        if matrix.bomb(cell[0], cell[1]):
            return _find_from_hit(cell[0], cell[1], matrix)


iterations = int(sys.argv[1])
n = int(sys.argv[2])
matrixes = [Matrix(n) for i in range(iterations)]


print("Running {0} test iterations with matrix "
      "size {1}*{1}\n".format(iterations, n))


run_test(bruteforce, matrixes)
run_test(smart_bruteforce, matrixes)

print("\n")

run_test(bruteforce_until_hit, matrixes)
run_test(random_until_hit, matrixes)
run_test(one_out_of_three_until_hit, matrixes)
run_test(one_out_of_three_until_hit_random, matrixes)

_find_from_hit = _find_from_hit_border
print("\nPatched _find_from_hit() to take border into account.\n")
run_test(bruteforce_until_hit, matrixes)
run_test(random_until_hit, matrixes)
run_test(one_out_of_three_until_hit, matrixes)
run_test(one_out_of_three_until_hit_random, matrixes)

Matrix._bomb = Matrix.bomb
Matrix.bomb = bomb_with_cache
print("\nPatching bomb() to never bomb twice the same cell.\n")
run_test(bruteforce_until_hit, matrixes)
run_test(random_until_hit, matrixes)
run_test(one_out_of_three_until_hit, matrixes)
run_test(one_out_of_three_until_hit_random, matrixes)
