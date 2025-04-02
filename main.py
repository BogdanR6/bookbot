def get_book_text(file_path: str) -> str:
    with open(file_path, "r") as file:
        return file.read()
    return ""


def main():
    print(get_book_text("books/frankenstein.txt"))


if __name__ == "__main__":
    main()
