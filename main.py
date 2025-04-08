import sys

from stats import get_num_words
from stats import get_count_char
from stats import sort_dic

def main():

    if len(sys.argv) > 1:
        books_path = sys.argv[1]
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    text = get_book_text(books_path)
    num_words = get_num_words(text) 
    char_count = sort_dic(get_count_char(text))

    # --- 
    print("=== BOOKBOT ===")
    print(f"Analyzing book found at {books_path}...")
    print("--- Word Count ---")
    print(f"Found {num_words} total words")
    print("--- Character Count ---")
    
    for item in char_count:
        char = item["char"]
        count = item["count"]
        
        if char.isalpha():
            print(f"{char}: {count}")
    # ---
    

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

main()
