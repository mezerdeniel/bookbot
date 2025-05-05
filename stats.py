def get_num_words(text):
    words = text.split()
    count = len(words)
    return count

def count_chars(text):
    lower_chars = text.lower()
    char_count = {}

    for char in lower_chars:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_char_dict(counted_chars):
    dict_list_chars = []
    for char, num in counted_chars.items():
        if char.isalpha():
            dict_list_chars.append({'char': char, 'num': num})
    dict_list_chars.sort(key=lambda x: x['num'], reverse=True)       
    return dict_list_chars
