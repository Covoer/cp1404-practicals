from guitar import Guitar


def main():
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another_guitar = Guitar("Another Guitar", 2013, 1000)

    print("Gibson L-5 CES get_age() - Expected 101. Got", guitar.get_age())
    print("Another Guitar get_age() - Expected 10. Got", another_guitar.get_age())
    print("Gibson L-5 CES is_vintage() - Expected True. Got", guitar.is_vintage())
    print("Another Guitar is_vintage() - Expected False. Got", another_guitar.is_vintage())


if __name__ == '__main__':
    main()