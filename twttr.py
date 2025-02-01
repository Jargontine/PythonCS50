n=input("Input:")
print("Output:",end="")
for i in n:
    if not i.lower() in ["a","e","i","o","u"]:
        print(i,end="")
print()