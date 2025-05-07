from stats import get_book_text
from stats import count_characters
from stats import dict_to_list
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        with open(sys.argv[1]) as f:
            # f is a file object
            file_contents = f.read()
            print("============ BOOKBOT ============")
            print(f"Analyzing book found at {sys.argv[1]}")
            print("----------- Word Count ----------")
            
            word_count = get_book_text(file_contents)
            
            print(f"Found {word_count} total words")
            print("--------- Character Count -------")
            
            char_count = count_characters(file_contents)
            sorted_char_count = dict_to_list(char_count)
            
            for char, count in sorted_char_count:
                if char.isalpha():
                    print(f"{char}: {count}")

            print("============= END ===============")

main()