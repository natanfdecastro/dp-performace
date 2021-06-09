def gold_mine_dp():
    print("parse")


def gold_mine_brute_force():
    print("parse")

a=[]
f=[]
print("enter elements")
for i in range(0,3):
    b=[]
    p=[]
    for j in range(0,3):
        c=int(input())
        b.append(c)
        p.append(0)
    a.append(b)
    f.append(p)
print("entered matrix is")
"""k=[]
for i in range(0,3):
    k.append(a[i][0])
max=max(k)
"""
maxi=max(a[0][0],a[1][0],a[2][0])
for i in range(0,3):
    if maxi==a[i][0]:
        f[i][0]=maxi
        break
for j in range(0,3):
    for i in range(0,3):
        if a[i][j]==maxi:
            if i==0 and j<2:
                top=0
                mid=a[i][j+1]
                bottom=a[i+1][j+1]
            elif i==1 and j<2:
                top=a[i-1][j+1]
                mid=a[i][j+1]
                bottom=a[i+1][j+1]
            elif i==2 and j<2:
                bottom=0
                mid=a[i][j+1]
                top=a[i-1][j+1]
            maxi=max(bottom,mid,top)

            if maxi==bottom and j<2:
                f[i+1][j+1]=a[i+1][j+1]
            elif maxi==top and j<2:
                f[i-1][j+1]=a[i-1][j+1]
            elif maxi==mid and j<2:
                f[i][j+1]=a[i][j+1]
for i in range(0,3):
    print(a[i])
print("\n")
for i in  range(0,3):
    print(f[i])
