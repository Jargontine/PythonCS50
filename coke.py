n=50
while n>0:
    print("Amount Due:",n)
    i=int(input("Insert Coin:"))
    if i in [25,10,5]:
        n-=i
change=abs(n)
print("Change Owed:",change)