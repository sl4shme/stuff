"""
Given a string, return a how many time a given substring is present.
The substring could be overlapping.
Examples:
    plop_plop_test plop => 2
    ploploptest plop => 2
    testploploptest plop => 2
"""


def find_with_overlap(s, r, count=0):
    """
    With recursion
    """
    occurence = s.find(r)
    if occurence == -1:
        return count
    else:
        count += 1
        return find_with_overlap(s[occurence + 1:], r, count)


def find_with_overlap_2(s, r):
    """
    With find("sub", start=...)
    """
    count = start = 0
    while 1:
        start = s.find(r, start) + 1
        if start > 0:
            count += 1
        else:
            return count


tests = ["plop_plop_test", "ploploptest", "testploploptest", "testtest"]
for test in tests:
    print("{} : {}".format(test, find_with_overlap(test, "plop")))

for test in tests:
    print("{} : {}".format(test, find_with_overlap_2(test, "plop")))
