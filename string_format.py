n = int(raw_input())
step = len(bin(n).replace('0b',' '))

for i in range(1,n+1):
    print "{0:d}{0:{width}o}{0:{width}X}{0:{width}b}".format(i, width=step)

