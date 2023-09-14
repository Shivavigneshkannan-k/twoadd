n="abcdefghijk"
newlist=[]
for i in range(len(n)):
  for j in range(len(n)-1,0,-1):
    if n[i] not in newlist and n[j] not in newlist:
      if n[i]==n[j]:
        newlist.append(n[i] or n[j])
      else:
        # print("i=>",i,"j=>",j)
        newlist.extend([n[i],n[j]])
for k in newlist:
  print(k,end=" ")