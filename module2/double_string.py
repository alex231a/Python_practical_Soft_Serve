import re

import re


def double_string(data):
    count = 0
    pattern = "^(" + "|".join(data) + ")(" + "|".join(data) + ")$"
    print(pattern)

    for s in data:
        if re.match(pattern, s):
            count += 1

    return count


data = ['aa', 'aaaa', 'abc', 'abcabc', 'qwer', 'qwerqwer']
print(double_string(data))

data = ['aa', 'abc', 'qwerqwer']
print(double_string(data))

data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qwerqwert']
print(double_string(data))

data = ['aa', 'aaaa', 'aaaaaaaa', 'aaaa', 'qwer', 'qweraaaa']
print(double_string(data))