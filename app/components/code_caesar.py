import string 

def code_caesar(text, decalage):
    lowercase = list(string.ascii_lowercase)
    new_alph_lower = {ch:lowercase[(i+decalage)%26] for i, ch in enumerate(lowercase)}
    uppercase = list(string.ascii_uppercase)
    new_alph_upper = {ch:uppercase[(i+decalage)%26] for i, ch in enumerate(uppercase)}
    case = lowercase + uppercase
    new_alph = new_alph_lower | new_alph_upper
    text_list = text.split(' ')
    words_list = [list(word) for word in text_list]

    new_text = []
    for char_list in words_list:
        new_list = []
        for char in char_list:
            if char in case:
                new_list += new_alph[char]
            else:
                new_list += char
        new_text.append(''.join(new_list))
    new_text = ' '.join(new_text)
    return new_text