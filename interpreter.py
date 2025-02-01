def main():
    arth = input("Expression: ")

    convert(arth)

def convert(s):
    split = s.split(" ")

    x = float(split[0].replace("[]", " "))

    z = float(split[2].replace("[]", " "))

    y = split[1].replace("[]", "")

    if y == "+":
        print(x + z)

    elif y == "-":
        print(x - z)

    elif y == "*":
        print(x * z)

    elif y == "/":
        print(x / z)
    else:
        print("Invalid operator")

main()