from stats import get_number_of_words
from stats import num_of_letters
from stats import chars_dict_to_sorted_list
import sys


BANNER = r"""
  ____              _     ____       _
 | __ )  ___   ___ | | __| __ )  ___| |_
 |  _ \ / _ \ / _ \| |/ /|  _ \ / _ \ __|
 | |_) | (_) | (_) |   < | |_) | (_) | |_
 |____/ \___/ \___/|_|\_\|____/ \___/ \__|
"""

print(BANNER)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def print_report(path, num_words, final_sort):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character, count in final_sort:
        if character.isalpha():
            print(f"{character}: {count}")
    print("============= END ===============")


def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    text = get_book_text(path)

    num_words = get_number_of_words(text)
    char_counts = num_of_letters(text)
    final_sort = chars_dict_to_sorted_list(char_counts)
    print_report(path, num_words, final_sort)
main()
