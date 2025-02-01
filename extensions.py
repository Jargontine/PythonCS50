i=input("File name: ").lower().strip()
if i.endswith(".gif"):
    print("image/gif")
elif i.endswith(".jpg"):
    print("image/jpeg")
elif i.endswith(".jpeg"):
    print("image/jpeg")
elif i.endswith(".png"):
    print("image/png")
elif i.endswith(".pdf"):
    print("application/pdf")
elif i.endswith(".txt"):
    print("text/plain")
elif i.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")