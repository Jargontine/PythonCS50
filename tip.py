def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    dolarrr=d.replace("$","")
    return float(dolarrr)

def percent_to_float(p):
    parcinttt=p.replace("%","")
    parcinttt_converted=float(parcinttt)/100
    return parcinttt_converted

main()