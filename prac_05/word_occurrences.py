def main():
    """
    Program to count occurrences of words in a string and print them.
    Time estimate: Approximately 15 minutes.
    """
    text = input("Text: ")
    words = text.split()

    # Create a dictionary to store word counts
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Sort the words for display
    sorted_words = sorted(word_count.keys())

    # Find the longest word for formatting purposes
    max_length = max([len(word) for word in sorted_words])

    # Display the word counts
    for word in sorted_words:
        print(f"{word:>{max_length}} : {word_count[word]}")


if __name__ == "__main__":
    main()
