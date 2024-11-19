def main():
    book_path = "books/frankenstein.txt"
    with open(book_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        # print(len(words))
        # print(file_contents)
        map = {}
        lowerd_characters = file_contents.lower()
        for c in lowerd_characters:
            map[c.lower()] = map.get(c.lower(), 0) + 1
        print(f"--- Begin report of {book_path} ---")
        print(f"{len(words)} words found in the document")
        for char in map:
            if char == '\n':
                print(f"The '\\n' character was found {map[char]} times")
            else:
                print(f"The '{char}' character was found {map[char]} times")
        print("--- End report ---")



if __name__ == "__main__":
    main()