import sys
from stats import count_words, count_chars, sort_count_chars

@staticmethod
def get_book_txt(filepath: str) -> str:
    file_content = ""
    with open(filepath) as f:
        file_content = f.read()
    return file_content


def main(arg):
    if not arg:
        return
    book_content = get_book_txt(filepath=arg)
    num_words = count_words(book_content)
    char_count = count_chars(book_content)
    storted_chars = sort_count_chars(char_count)
    print(
    f"""============ BOOKBOT ============\n
Analyzing book found at {arg}...\n
----------- Word Count ----------\n
Found {num_words} total words\n
--------- Character Count -------"""
)
    for item in storted_chars:
        print(f"{item["char"]}: {item["num"]}")
        
if __name__ == "__main__":
    args = sys.argv
    if args[1]:
        arg = args[1]
    main(arg)