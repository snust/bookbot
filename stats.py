def get_book_text(text):
    words = text.split()
    num_words = len(words)
    return num_words

def count_characters(text):
    count = {}

    for char in text.lower():
        count[char] = count.get(char, 0) + 1
    
    return count

def dict_to_list(d):
    return [(k, v) for k, v in sorted(d.items(), key=lambda item: item[1], reverse=True)]