a=input("what is the answer to the great question of life, the Universe , and Everything? ")
if a.strip()=="42":
    print("Yes")
elif a.lower().strip()=="forty-two":
    print("Yes")
elif a.lower().strip()=="forty two":
    print("Yes")
else:
    print("No")
