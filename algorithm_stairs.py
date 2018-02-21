from __future__ import print_function
n = int(raw_input().strip())

for i in range(n,0,-1):
    print(" "*(i-1), "#"*(n+1-i), sep="")