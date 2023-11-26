import wikipedia

while True:
    try:
        title = input("Enter a page title or search phrase (or press enter to quit): ")
        if not title:
            break

        page = wikipedia.page(title, auto_suggest=False)
        print(f"Title: {page.title}\nSummary: {page.summary}\nURL: {page.url}\n")

    except wikipedia.DisambiguationError as e:
        print(f"Disambiguation error: {e.options}")
    except wikipedia.PageError:
        print("Page not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
