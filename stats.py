def get_number_of_words(text):
    words = text.split()
    return len(words)

def num_of_letters(book):
    counts = {}

    for letter in book:
        lowercase_letter = letter.lower()
        if lowercase_letter in counts:
            counts[lowercase_letter] += 1
        else:
            counts[lowercase_letter] = 1

    return counts


def sort_on(letter):
    return letter[1]

def chars_dict_to_sorted_list(counts):
    chars_list = []
    for character in counts:
        quantity = counts[character]
        chars_list.append((character, quantity))
    sorted_chars_list = sorted(chars_list, reverse=True, key=sort_on)
    return sorted_chars_list

