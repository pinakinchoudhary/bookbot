import sys
from stats import get_book_text, char_dict, sorted_dict

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    num_words = len(get_book_text(path).split())
    print(f"""============ BOOKBOT ============
Analyzing book found at {path}...
----------- Word Count ----------""")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    new = {}
    new = char_dict(get_book_text(path).lower())
    # print(new)
    for pair in sorted_dict(new):
        print(pair['char'] + ":", pair['num'])
    print("============= END ===============")

main()

