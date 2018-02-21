import string

n = 5
list_abc = list(string.ascii_lowercase)
for i in range(len(list_abc)):
    if i <= (n-1):
        print list_abc[i]

