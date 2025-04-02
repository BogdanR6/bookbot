def get_number_of_words(text: str) -> int:
    return len(text.split())


def get_char_count_dict(text: str) -> dict:
    text = text.lower()
    char_count = {}
    for char in text:
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count


def sort_char_count_dict(char_count: dict) -> dict:
    return dict(sorted(char_count.items(), key=lambda item: item[1], reverse=True))
