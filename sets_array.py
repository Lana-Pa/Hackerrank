# Code that works in hackerrank

n, m = raw_input().split()

sc_ar = raw_input().split()

A = set(raw_input().split())
B = set(raw_input().split())
print sum((i in A) - (i in B) for i in sc_ar)

# n, m = raw_input().split()
# ar = map(int,raw_input().split())
# set_a = set(map(int,raw_input().split()))
# set_b = set(map(int,raw_input().split()))
#
# set_ar = set(ar)
# array = list(set_ar)
#
# happiness = 0
#
# for i in array:
#     if i in set_a:
#         happiness +=1
#     if i in set_b:
#         happiness -=1
# print happiness