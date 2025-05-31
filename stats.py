def get_num_words(text):
    words = text.split()   
    return (len(words))

def get_total_characters(text):
    characters = {}
    for character in text:
        lowercase = character.lower()
        if lowercase in characters:
            characters[lowercase] += 1
        else:
            characters[lowercase] = 1
    return characters

def sort_total_characters(characters):
    list_of_characters = []
    for character in characters:
        list_of_characters.append({"char": character, "num": characters[character]})
    return list_of_characters

def sort_on(dict):
    return dict["num"]