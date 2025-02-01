def calculate_percentage(x, y):
    percentage = (x / y) * 100
    return round(percentage)

def fuel_status():
    while True:
        try:
            fraction_input = input("Enter a fraction (X/Y): ")
            x, y = map(int, fraction_input.split('/'))

            if x < 0 or y <= 0 or x > y:
                print("invald input")
                continue

            percentage = calculate_percentage(x, y)

            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break

        except ValueError:
            print("Invalid input. Please enter integers separated by '/'.")

        except ZeroDivisionError:
            print("Invalid input. The denominator (Y) cannot be zero.")

if __name__ == "__main__":
    fuel_status()
