"""
Given a list of integers from 0 to 99 (for example: [0,1,2,50,52,75])
Produce a string that describes numbers missing from the list (for example:
"3-49,51,53-74,76-99")

Ex:
    [] => "0-99"
    [0] => "1-99"
    [3, 5] => "0-2,4,6-99
"""


def print_missing(l):
    missing = [i for i in range(100) if i not in l]
    result = []
    last = None
    for index, val in enumerate(missing):
        try:
            if val + 1 == missing[index + 1]:
                if last is not None:
                    continue
                else:
                    last = val
            else:
                if last is None:
                    result.append(str(val))
                else:
                    result.append(str(last) + "-" + str(val))
                    last = None
        except IndexError:
            if last is None:
                result.append(str(val))
            else:
                result.append(str(last) + "-" + str(val))
    print(",".join(result))


print_missing([0, 1, 2, 50, 52, 75])
print_missing([3, 5])
print_missing([])
print_missing([0])
print_missing([50])
print_missing([99])
print_missing([98, 99])
print_missing([0, 99])
print_missing([1, 98])
print_missing([1, 97, 98])
