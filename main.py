from stats import get_num_words, get_char_count, dict_to_list
import sys



def get_books_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main(book):
    text = get_books_text(book)
    num_words = get_num_words(text)
    char_count = get_char_count(text)
    sorted_count = dict_to_list(char_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_count:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")

    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        main(sys.argv[1])


