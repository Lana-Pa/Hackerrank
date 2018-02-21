arr = map(int, raw_input().strip().split(' '))
ar_s = sorted(arr)
sum_min = 0
sum_max = 0
print ar_s

for i in range(len(ar_s)-1):
    sum_min = sum_min + ar_s[i]

for i in range(1,len(ar_s)):
    sum_max = sum_max + ar_s[i]

print sum_min, sum_max
