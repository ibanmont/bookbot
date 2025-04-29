def num_words(text):
    words = text.split()
    return len(words)


# Creates dictionary with character as "key" and the count as "value"
def char_count(text):
    char_count = {}

    for char in text:
        low_char = char.lower()
        if low_char in char_count:
            char_count[low_char] += 1
        else:
            char_count[low_char] = 1
    
    return char_count

    # Creates the value used for "key" in the ".sort" method.
def sort_on(input_dict):
    return input_dict["num"]


# Breaksdown dictionary and makes list of dictionaries that we can sort
def sort_list_of_d(input_dict):
    list_of_dicts = []

    for key, value in input_dict.items():
        new_dict = {"char": key, "num": value}
        list_of_dicts.append(new_dict)

    list_of_dicts.sort(reverse=True, key=sort_on)
    
    return list_of_dicts