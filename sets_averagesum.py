number = raw_input()
astring = raw_input().split()

astr = map(int,astring)
aset = set(astr)

count = float(len(set(aset)))
summ = float(sum(aset))

print summ / count