def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def word_count(filepath):
    text = get_book_text(filepath)
    word_list = text.split()
    return len(word_list)

def char_count(filepath):
    text = get_book_text(filepath)
    char_count_dict = {}
    for char in text:
        char = char.lower()
        if char in char_count_dict:
            char_count_dict[char] += 1
        else:
            char_count_dict[char] = 1
    return char_count_dict

def sorted_char_count(filepath):
    cc_dict = char_count(filepath)
    dict_list = []
    for char in cc_dict:
        new_dict = {"char": char, "num": cc_dict[char]}
        dict_list.append(new_dict)
    dict_list.sort(reverse=True, key=lambda a: a["num"])
    return dict_list
