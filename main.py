from stats import get_num_words, get_char_count

def get_books_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def main(book):
    text = get_books_text(book)
    num_words = get_num_words(text)
    print(f"{num_words} words found in the document")

    char_count = get_char_count(text)
    print(char_count)

main("books/frankenstein.txt")

