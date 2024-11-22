import re

text = "Hello Dave"
pattern = r"Hello"
result = re.match(pattern, text)

print(result)