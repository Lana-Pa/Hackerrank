# Mark and Jane are very happy after having their first kid. Their son is very fond of toys, so Mark wants to buy some.
# There are  different toys lying in front of him, tagged with their prices, but he has only . He wants to maximize the
# number of toys he buys with this money.
#
# Now, you are Mark's best friend and have to help him buy as many toys as possible.
#
# Input Format
#
# The first line contains two integers,  and , followed by a line containing  space separated integers indicating the products' prices.


n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
prices = map(int, raw_input().strip().split(' '))
prices_sort = sorted(prices)

quant = 0
summ = 0
for i in prices_sort:
    if summ <= k and i < (k-summ):
        summ = summ + i
        quant += 1
    if summ > k: break

print quant
