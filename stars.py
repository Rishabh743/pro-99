name=input("enter your name")
iter=len(name)
for i in range(0,iter):
    for j in range(0,iter):
        if i==j:
         print(name[i],sep=" ",end=" ")
        else:print("*",sep=" ",end=" ") 
    print()
        