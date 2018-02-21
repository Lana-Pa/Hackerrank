n = int(raw_input().strip())
grades = []
grades_i = 0
for grades_i in xrange(n):
    grades_t = int(raw_input().strip())
    grades.append(grades_t)

for x in grades:
    for i in range(x,x+5):
        if i%5 == 0:
            mult = i
    if (mult - x) < 3:
        result = mult
    if x < 38 or (mult-x) >= 3:
        result = x
    print result
