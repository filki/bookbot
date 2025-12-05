from stats import count_book_words, count_chars, sorter
import sys
def get_book_text(filepath: str):
    with open (filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    if len(sys.argv) != 2:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    words = count_book_words(book)
    chars = count_chars(book)
    sorted_chars = sorter(chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print('============= END ===============')
main()