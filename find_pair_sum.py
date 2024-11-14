def find_pair(a,z,n):
    for i in range(n):
        for j in range(n):
            if (i!=j and a[i]*a[j]==z):
                print(a[i]*a[j])
                return True
    return False

a=[1,2,1,0,5]
z=10
n=len(a)

if (find_pair(a,n,z)):
    print("true")
    
else:
    print("false")