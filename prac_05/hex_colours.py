# Dictionary of colour names to hexadecimal codes
COLOUR_TO_HEX = {
    "AliceBlue": "#f0f8ff",
    "AntiqueWhite": "#faebd7",
    "Aqua": "#00ffff",
    "Aquamarine": "#7fffd4",
    "Azure": "#f0ffff",
    "Beige": "#f5f5dc",
    "Bisque": "#ffe4c4",
    "Black": "#000000",
    "BlanchedAlmond": "#ffebcd",
    "Blue": "#0000ff"
}


def main():
    print("Hexadecimal Colour Lookup\n")
    colour_name = input("Enter colour name (or blank to quit): ")
    while colour_name != "":
        hex_code = COLOUR_TO_HEX.get(colour_name.strip().capitalize())
        if hex_code:
            print(f"{colour_name.capitalize()} has the code {hex_code}")
        else:
            print("Invalid colour name")
        colour_name = input("Enter colour name (or blank to quit): ")


if __name__ == "__main__":
    main()
