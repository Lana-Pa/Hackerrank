n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))

lowest = ar[0]
highest = ar[0]
broke_h = 0
broke_l = 0
for i in range(len(ar)):
    if ar[i]>highest:
        highest = ar[i]
        broke_h += 1
    if ar[i]<lowest:
        lowest = ar[i]
        broke_l += 1

print broke_h, broke_l