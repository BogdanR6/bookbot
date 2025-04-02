# BookBot

BookBot is a simple command-line tool that analyzes a text file (e.g., a book) and provides statistics such as word count and character frequency.

## Features

- Counts the total number of words in the given text file.
- Analyzes the frequency of each alphabetical character.
- Sorts character frequency in descending order.

## Installation

This script requires Python 3.

1. Clone this repository:

   ```sh
   git clone <repository-url>
   cd <repository-name>
   ```

2. Ensure you have the required module (`stats.py`) in the same directory.

## Usage

Run the script with the path to the book file as an argument:

```sh
python3 bookbot.py <path_to_book>
```

### Example

```sh
python3 bookbot.py example.txt
```

**Output:**

```
============ BOOKBOT ============
Analyzing book found at example.txt...
----------- Word Count ----------
Found 12345 total words
--------- Character Count -------
a: 456
b: 234
...
============= END ===============
```

## Dependencies

- Python 3.x
- `stats.py` (containing `get_number_of_words`, `get_char_count_dict`, and `sort_char_count_dict` functions)

## Author
Bogdan Rares
