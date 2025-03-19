
def get_num_words(text):
    word_list = text.split()
    num_words = len(word_list)
    return num_words

def get_char_count(text):
    char_count = {}
    low_text = text.lower()
    for char in low_text:
        char_count[char] = char_count.get(char, 0) + 1
    
    return char_count
