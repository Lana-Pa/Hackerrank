# You are given a string . Your task is to capitalize each word of
#Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

import re

h = raw_input()
m = re.split(r'(\s+)',h)

hh=list()

for i in m:
    i = i.capitalize()
    hh.append(i)

print ''.join(hh)
