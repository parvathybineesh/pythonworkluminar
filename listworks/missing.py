lst=[3,1,5,6,4]
lst.sort()
for i in range(0,len(lst)):
    current=lst[i]
    next=lst[i+1]
    diff=next-current
    if diff !=1:
        print(current+1,"is missing")
        break
