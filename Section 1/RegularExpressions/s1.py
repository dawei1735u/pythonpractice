import re

text = "Hello Dave"
pattern = r"Dave"
result = re.match(pattern, text)

print(result)