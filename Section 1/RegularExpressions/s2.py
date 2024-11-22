import re

text = "Hello World God Is Totally Awesome, I am TRULY Grateful"

pattern = r"TRULY"

result = re.search(pattern, text)

if result:
    print(result.group())

