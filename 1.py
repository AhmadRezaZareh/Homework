import time 

x = int(input("enter time:"))

print (x)


s = int(x%60)
m = int((x/60)%60)
h = int ((x/3600))


print(f"{h:00}:{m:00}:{s:00}")
