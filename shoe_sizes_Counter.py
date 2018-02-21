
# Rahue is a shoe shop owner. His shop has N number of shoes.
# He has a list containing the size of each shoe he has in his shop.
# There are n number of customers who are willing to pay  amount of money only if
# they get the shoe of their desired size.
#
# Your task is to compute how much money Rahue earned.
#
# Input Format
#
# The first line contains , the number of shoes.
# The second line contains the space separated list of all the shoe sizes in the shop.
# The third line contains , the number of customers.
# The next  lines contain the space separated values of the  desired by the customer and , the price of the shoe.


from collections import Counter

N = int(raw_input('Enter number of shoes: '))
sizes = Counter(map(int,raw_input('Enter all shoes sizes: ').split())) # list of shoe sizes and their quantity
n = int(raw_input('Enter number of customers: '))

total = 0

for i in range(n):
    pair = map(int, raw_input('Enter size-price: ').split())  # list (size, price)
    size = pair[0]
    price = pair[1]
    if size in sizes.keys() and sizes[size]!=0:
        total = total+price
        sizes[size] = sizes[size] - 1
    else:
        continue

print total






# myList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
# print Counter(myList)
#
# print Counter(myList).items()
#
# print Counter(myList).keys()
#
# print Counter(myList).values()
