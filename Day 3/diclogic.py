word_counts = {}

def add_word(word):
    if word in word_counts.keys():
        word_counts[word] = word_counts[word]+1
    else:
        word_counts[word] = 1
    return word_counts

def view_all_words(word):
       return word_counts

def view_all_counts(word):
    if not word_counts:
        return "No words added yet"
    else:
        for word, count in word_counts.items():
            return word, count

def view_words_with_count(count):
    filtered_words = [word for word, word_count in word_counts.items() if word_count == count]
    if not filtered_words:
        return "No words found with that count"
    else:
        for word in filtered_words:
            return word


