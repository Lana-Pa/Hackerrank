n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))
l = len(arr)
count_pos = 0
count_neg = 0
count_zero = 0
for i in arr:
    if i > 0:
        count_pos += 1
    if i < 0:
        count_neg += 1
    if i == 0:
        count_zero += 1
pos = float(count_pos)/float(l)
neg = float(count_neg)/float(l)
zer = float(count_zero)/float(l)
float(count_pos)/float(l), float(count_neg)/float(l), float(count_zero)/float(l)

print "%.6f" % pos
print "%.6f" % neg
print "%.6f" % zer