# https://www.hackerrank.com/challenges/compare-the-triplets?h_r=next-challenge&h_v=zen


triplet_A = map(int, raw_input().strip().split(' '))
triplet_B = map(int, raw_input().strip().split(' '))
Alice_sum = 0
Bob_sum = 0

for a, b in zip(triplet_A, triplet_B):
    if a > b:
        Alice_sum += 1
    if a < b:
        Bob_sum += 1
    if a == b:
        continue
if Alice_sum == Bob_sum == 0:
    print ""
else:
    print Alice_sum, Bob_sum


