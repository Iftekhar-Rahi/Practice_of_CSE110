sum=0
for i in range (1,601):
    if i%7==0 and i%9==0:
        sum+=i
print(sum)