import string


def clean_words(words):
    result = []
    for word in words:
        for symbol in word:
            if symbol in string.punctuation:
                word = word.replace(symbol, '')
        result.append(word.lower())
    return result


def get_second(element):
    return element[1]


def count_words(words):
    unique_words = set(words)
    words_counter = {}
    for word in unique_words:
        words_counter[word] = words.count(word)
    items = words_counter.items()
    items = sorted(items, key=lambda x: x[1], reverse=True)
    return items[:10]


def top_10(text):
    words = text.split()
    words = clean_words(words)
    top = count_words(words)
    print('Топ-10 слов:')
    for word, num in top:
        print('%s : %d' % (word, num))


top_10('Привет! Я питон но я не простой питон A #Python!')
