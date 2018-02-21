import sys

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
print ar.count(max(ar))