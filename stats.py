
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

def sort_on(char_count):
    return char_count["count"]

def dict_to_list(char_count):
    list_of_dicts = []

    for char, count in char_count.items():
        list_of_dicts.append({"char": char, "count": count})

    list_of_dicts.sort(reverse=True, key=sort_on)

    return list_of_dicts