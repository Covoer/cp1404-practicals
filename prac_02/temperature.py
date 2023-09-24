def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = get_celsius()
            fahrenheit = convert_celsius(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            # TODO: Write this section to convert F to C and display the result
            # Hint: celsius = 5 / 9 * (fahrenheit - 32)
            # Remove the "pass" statement when you are done. It's a placeholder.
            fahrenheit = get_fahrenheit(fahrenheit)
            celsius = convert_fahreheit(celsius, fahrenheit)
            print(f"Result: {celsius: .2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahreheit(celsius, fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def get_fahrenheit(fahrenheit):
    fahrenheit = float(input("Fahrenheit: "))
    return fahrenheit


def convert_celsius(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


def get_celsius():
    celsius = float(input("Celsius: "))
    return celsius


main()