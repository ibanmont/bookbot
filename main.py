import sys

from stats import (
    num_words, 
    char_count, 
    sort_list_of_d
)

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]

    # The "sys.argv" code is meant to replace the hard coded path below:
    # book_path = "books/frankenstein.txt"
    
    text = get_book_text(book_path)
    word_total = num_words(text)
    character_count_dict = char_count(text)
    sorted_list_of_d = sort_list_of_d(character_count_dict)
    print_report(book_path, word_total, sorted_list_of_d)
    
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def print_report(book_path, word_total, sorted_list_of_d):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    print("----------- Word Count ----------")
    print(f"Found {word_total} total words")

    print("--------- Character Count -------")
    for item_dict in sorted_list_of_d:
        if item_dict["char"].isalpha() is True:
            print(f"{item_dict["char"]}: {item_dict["num"]}")
    
    print("============= END ===============")


# All def functions are created before the main def is called here.

main()