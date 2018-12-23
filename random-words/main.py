import random
import json


MAX_COUNT = 1000


def load_words():
    with open("google-10000-english-usa-no-swears.txt") as word_file:
        valid_words = word_file.read().split()

    return valid_words


def get_count(request):
    '''Extracts 'count' from query string or JSON passed in the request.'''
    # Check if 'count' was passed as a query parameter.
    if request.args and "count" in request.args:
        return request.args.get("count")

    # Check if 'count' was passed via JSON.
    request_json = request.get_json()
    if request_json and "count" in request_json:
        return request_json["count"]

    # Default count is "1".
    return 1


def random_words(request):
    count = get_count(request)

    # count may be a string, try to convert it to an integer.
    if type(count) is not int:
        try:
            count = int(count)
        except ValueError:
            return f"count: {count} is not valid input."

    # Ensure count does not exceed maximum.
    if count > MAX_COUNT:
        count = MAX_COUNT

    # Read list of words into memory.
    words = load_words()

    # Collect some unique random words.
    unique_random_words = set()
    while len(unique_random_words) != count:
        random_word = random.choice(words)
        unique_random_words.add(random_word)

    # Return the set of words as JSON.
    # Python cannot automatically serialize a set (so convert to a list first).
    return json.dumps(list(unique_random_words))
