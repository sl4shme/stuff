"""
Print the five most apearing words in a given file.

If multiple words share the same count, print them on the same line.

Example:
    plop.txt
        plop plop plip test
        test plop plip
        haha

    output:
        plop
        plip test
        haha
"""
import io
import re


def build_words_dict(f):
    if not isinstance(f, io.IOBase):
        f = open(f)
    words = {}
    for line in f.readlines():
        # Clean any non alphanum char
        line = re.sub("[^a-zA-Z0-9]", " ", line)
        # Remove multiple space
        line = re.sub("\s\s+", " ", line)
        for word in line.split():
            current = words.get(word, 0)
            words[word] = current + 1
    return words


def print_top_words(words):
    inverted = {}
    for word, count in words.items():
        inverted[count] = inverted.get(count, [])
        inverted[count].append(word)

    for idx, key in enumerate(sorted(inverted.keys(), reverse=True)):
        if idx < 5:
            print(" ".join(inverted[key]))
        else:
            break


# Testing

test_1_content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
culpa qui officia deserunt mollit anim id est laborum.
"""

test_2_content = """
plop plop plop aa aa aa aa aa bb bb bb bb bb bb bb
   plip test haha . / ./ plip [;122345] plip
dododada plip dodo;"dada  ";; plip
plip gg tt rr ee plip

plip

dada didi
"""

test_3_content = ""

test_4_content = ";,.@ #$% ^^&%& %$#@   !&$ ^%"

test_cases = [test_1_content, test_2_content, test_3_content, test_4_content]

for test in test_cases:
    test_file = io.StringIO()
    test_file.write(test)
    test_file.seek(0)
    print_top_words(build_words_dict(test_file))
    print("\n")
