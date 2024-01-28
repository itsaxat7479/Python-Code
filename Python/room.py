su=0
for i in range(100,200):
    a=str(i)
    for y in a:
        k=int(y)
        su+=k
        if su%2==0:
            print(f"{i} is even and sum={su}")
    su=0
    
    
