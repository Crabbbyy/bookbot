import sys

def main():
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    characters = get_total_characters(text)
    listed_characters = sort_total_characters(characters)
    listed_characters.sort(reverse=True, key=sort_on)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for listed_character in listed_characters:
        if listed_character["char"].isalpha():
            print(f"{listed_character["char"]}: {listed_character["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
       return f.read()

from stats import get_num_words
from stats import get_total_characters
from stats import sort_total_characters
from stats import sort_on

if len(sys.argv) > 1:
    main()
else:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)