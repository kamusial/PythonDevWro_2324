from collections import Counter
import re


story = open("story.txt").read()
napis = "daspodk\\"
numbers_from_text = re.findall(r"\d", story)
print(numbers_from_text)


words = story.split()
print(Counter(words).most_common(5))
