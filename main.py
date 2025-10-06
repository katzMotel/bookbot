from stats import get_num_words
from stats import get_num_characters
from stats import chars_dict_to_sorted_list
import sys 
def main():
    if len(sys.argv) <2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    char_counts = get_num_characters(book_text)
    char_sorted_list = chars_dict_to_sorted_list(char_counts)
    print_report(book_path, num_words, char_sorted_list)
def get_book_text(filepath):
    with open(filepath, "r") as f:
        return f.read()

def print_report(book_path, num_words, char_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyizing book found at {book_path}...")
    print("----------- Word Count -----------")
    print(f"Found {num_words} total words")
    print("-------- Character Count ---------")
    for item in char_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item['char']}: {item['num']}")
    print("============ END ============")
main()