def wordcount(string_of_words):
    list_of_words = string_of_words.split()
    count = len(list_of_words)
    return count

def letter_count(text):
    l_text = text.lower()
    char_list = list(l_text)

    n_dict = {}
    seen = set()

    for char in char_list:
        if char not in seen:
            seen.add(char)

    for item in seen:
        count = 0
        for char in char_list:
            if char == item:
                count += 1
        
        n_dict[item] = count

    return n_dict

def sort_on(items):
    return items["num"]

def sort_dict(a_dict):
    n_list = []
    for item in a_dict:
        char = item
        count = a_dict[item]
        n_dict = {"char": char, "num" : count}
        n_list.append(n_dict)

    n_list.sort(reverse=True, key=sort_on)

    return n_list
