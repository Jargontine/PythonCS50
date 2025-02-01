i=input("Greeting: ")
ans=i.lower().strip()
if "hello" in ans:
    print("$0")
elif ans[0]=="h":
    print("$20")
else:
    print("$100")