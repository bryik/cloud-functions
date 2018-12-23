
import random

def load_words():
    with open('google-10000-english-usa-no-swears.txt') as word_file:
        valid_words = word_file.read().split()

    return valid_words


def random_word(request):
    words = load_words()
    return random.choice(words)

