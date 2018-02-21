s = raw_input()
alnum_true = 0
alpha_true = 0
digit_true = 0
lower_true = 0
upper_true = 0

for i in s:
    if i.isalnum()==True:
        alnum_true += 1
    if i.isalpha()==True:
        alpha_true += 1
    if i.isdigit()==True:
        digit_true += 1
    if i.islower()==True:
        lower_true += 1
    if i.isupper()==True:
        upper_true += 1

if alnum_true > 0:
    print 'True'
else:
    print 'False'

if alpha_true > 0:
    print 'True'
else:
    print 'False'

if digit_true > 0:
    print 'True'
else:
    print False

if lower_true > 0:
    print 'True'
else:
    print False

if upper_true > 0:
    print 'True'
else:
    print False

