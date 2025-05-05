from stats import get_num_words
from stats import count_chars
from stats import sort_char_dict
import sys



def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

    book_path = sys.argv[1]

    text = get_book_text(book_path)
    counted_words = get_num_words(text)
    counted_char = count_chars(text)
    sorted_chars = sort_char_dict(counted_char)


    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/frankenstein.txt...")

    print("----------- Word Count ----------")
    print(f"Found {counted_words} total words")

    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        print(f"{char_dict['char']}: {char_dict['num']}")
    
    print("============= END ===============")



if __name__ == "__main__":
    main()