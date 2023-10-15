def read_data(filename):
    """Read the data from the csv file and return as a list of lists."""
    data = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            data.append(line.strip().split(','))
    return data[1:]  # Exclude the header


def get_champions_and_counts(data):
    """Process the data to get champions and their win counts."""
    champions_count = {}
    for record in data:
        champion = record[1]  # Assuming the champion's name is in the 2nd column
        champions_count[champion] = champions_count.get(champion, 0) + 1
    return champions_count


def get_countries(data):
    """Extract the countries of the champions."""
    countries = set()
    for record in data:
        country = record[2]  # Assuming the country is in the 3rd column
        countries.add(country)
    return countries


def main():
    """Main function to read, process and display information."""
    data = read_data("wimbledon.csv")

    champions_count = get_champions_and_counts(data)
    print("Wimbledon Champions:")
    for champion, count in champions_count.items():
        print(f"{champion} {count}")

    countries = get_countries(data)
    print("\nThese {} countries have won Wimbledon:".format(len(countries)))
    print(", ".join(sorted(countries)))


if __name__ == "__main__":
    main()
