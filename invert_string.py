n = "lalala lala la"
new_list=[]
lengh = len(n)
for i in range(lengh):
    new_list.append(n[lengh-1])
    lengh -=1

print "".join(new_list)
