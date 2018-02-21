from __future__ import print_function
s = raw_input().strip()

hour = s[:2]
rest = s[2:8]
pm_am = s[8:]


if pm_am == "PM" and hour < "12":
    hour = int(hour) + 12

if hour == "12" and pm_am == "AM":
    hour = "00"

print(hour, rest,sep="")

