import re

test_str = "X-DSPAM-Confidence:0.8475"

print(re.match(r"^\b\d.\d+$", test_str))
print(test_str[:12])
print(test_str.split(":")[1])