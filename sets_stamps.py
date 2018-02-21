# Rupal has a huge collection of country stamps.
# She decided to count the total number of distinct country stamps in her collection.
# She asked for your help. You pick the stamps one by one from a stack of  country stamps.
#
# Find the total number of distinct country stamps.


N = int(raw_input())
country_set = set()
for i in range(N):
    country_set.add(raw_input())


print len(country_set)