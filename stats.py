def get_num_words(text):
    num_words = len(text.split())
    return f"Found {num_words} total words"

def get_num_characters(text):
    text = text.lower()
    char_count= {}
    for char in text:
        if char in char_count:
            char_count[char]+=1
        else:
            char_count[char]=1
    return char_count
def sort_on(d):
    return d["num"]
def chars_dict_to_sorted_list(char_counts):
    chars_list = []
    for char in char_counts:
        chars_list.append({"char": char, "num": char_counts[char]})
    chars_list.sort(reverse=True, key=sort_on)
    return chars_list