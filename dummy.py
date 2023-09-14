def addtwo(list1,target,newlist):
  for i in range(len(list1)):#i=0 element=1
    for j in range(len(list1)):#j=0 element=1
      if list1[i]+list1[j]==target:
        x=i
        y=j
  newlist.extend([x,y])
  print(newlist)
  
a=[1,2,3,4]
b=15
c=[]
addtwo(a,b,c)

