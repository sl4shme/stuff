"""
You are given an integer n
Your task is to print an alphabet rangoli of size n
(Rangoli is a form of Indian folk art based on creation of patterns.)

Different sizes of alphabet rangoli are shown below:
#size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

#size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------

#size 10
------------------j------------------
----------------j-i-j----------------
--------------j-i-h-i-j--------------
------------j-i-h-g-h-i-j------------
----------j-i-h-g-f-g-h-i-j----------
--------j-i-h-g-f-e-f-g-h-i-j--------
------j-i-h-g-f-e-d-e-f-g-h-i-j------
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
--j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
------j-i-h-g-f-e-d-e-f-g-h-i-j------
--------j-i-h-g-f-e-f-g-h-i-j--------
----------j-i-h-g-f-g-h-i-j----------
------------j-i-h-g-h-i-j------------
--------------j-i-h-i-j--------------
----------------j-i-j----------------
------------------j------------------
"""
al = 'abcdefghijklmnopqrstuvwxyz'


def make_line(n_start, n):
    line = al[n_start]
    for x in range(1, n):
        line += ("-" + al[n_start + x])
        line = (al[n_start + x] + "-") + line
    return line


def rangoli(n):
    lines = [make_line(0, n)]
    max_len = len(lines[0])

    for i in range(1, n):
        l = make_line(i, n - i)
        pad = int((max_len - len(l)) / 2)
        l = ("-" * pad) + l + ("-" * pad)
        lines.append(l)
        lines.insert(0, l)

    for line in lines:
        print(line)

rangoli(int(input()))
