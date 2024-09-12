

Amount = int(input("Enter sale price: "))
if(Amount>0):
    if Amount >=100:
        dis = Amount*0.10
    elif Amount <100:
        dis = Amount*0.05
    print("discount :",dis)
    print("net pay : ",Amount-dis)
else:
    print("Invalid Amount")