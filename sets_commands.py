# You have a non-empty set , and you have to execute  commands given in  lines.
# The commands will be pop, remove and discard.

# The first line contains integer , the number of elements in the set .
# The second line contains  space separated elements of set . All of the elements are non-negative integers, less than or equal to 9.
# The third line contains integer , the number of commands.
# The next  lines contains either pop, remove and/or discard commands followed by their associated value.
import random

N = int(raw_input())
sset = set(map(int,raw_input().split()))

for i in range(int(raw_input())):
    command = raw_input().split()
    if command[0] == "pop":
        sset.pop()
        print sset
    elif command[0] =="discard":
        sset.discard(int(command[1]))
        print sset
    elif command[0] =="remove":
        sset.remove(int(command[1]))
        print sset
print sset
print len(sset)

