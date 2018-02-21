# Given  sets of integers,  and , print their symmetric difference in ascending order.
# The term symmetric difference indicates those values that exist in either  or  but do not exist in both.

na = raw_input()
a = map(int,raw_input().split())
nb = raw_input()
b = map(int,raw_input().split())

seta = set(a)
setb = set(b)
a_dif = seta.difference(setb)
b_dif = setb.difference(seta)
sum_dif = sorted(a_dif | b_dif)

for x in sum_dif:
    print x

