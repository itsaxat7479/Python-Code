cp=int(input("enter the cost price amount:::"))
sp=int(input("enter teh sell price::::"))
print("the selling and cost price is price is->>",cp,sp) 
if cp>sp:
    profit=cp-sp
    print("Loss")
elif cp<sp:
    loss=sp-cp
    print("profit")
else:
    print("NO PROFIT NO LOSS JUST SAME FOR ")
    print("thanku for ")
