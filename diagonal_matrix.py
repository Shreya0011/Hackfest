count=1
lst=[]
n=int(input("no of list inside a list->"))
p=int(input("no of elements in side a list of list->"))
for i in range(n):
    x=[]
    print("taking the value of",count,"list")
    count=count+1
    for j in range(p):
        l=int(input("enter the no->"))
        x.append(l)
    lst.append(x)
print(lst)

print("printing the matrix")
for i in range(n):
    for j in range(p):
        print(lst[i][j],end=" ")
    print()


if n==p:
    print("printing the first ")
    for i in range(n):
        for j in range(i+1):
            print(lst[i][j],end=" ")
        print()

    print("printing the second matrix")
    for i in range(n):
        for k in range(n-i-1):
            print(" ",end=" ")
        for j in range(i + 1, 0, -1):
            print(lst[i][n - j], end=" ")
        print()
else:
    print("rows and coloum should be same")
