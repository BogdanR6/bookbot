import sys
from stats import get_number_of_words, get_char_count_dict, sort_char_count_dict


def get_book_text(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()
    return ""


def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 {sys.argv[0]} <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_number_of_words(text)} total words")
    print("--------- Character Count -------")
    char_count = sort_char_count_dict(get_char_count_dict(text))
    for char, count in char_count.items():
        if char.isalpha():
            print(f"{char}: {count}")

    print("============= END ===============")


if __name__ == "__main__":
    main()
