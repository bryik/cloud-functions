# random-words

This function is identical to `./random-word` except it can return multiple random English words from Google's list of the [10,000 most common words](https://github.com/first20hours/google-10000-english).

- There is a limit of 1000 words per request.
- The words returned in a request should be unique.
- The response is JSON encoded.

**Endpoint:** https://us-central1-omega-functions.cloudfunctions.net/random-words

## `GET`

```bash
curl -g https://us-central1-omega-functions.cloudfunctions.net/random-words?count=5
```

May return:

> ["languages", "dairy", "separately", "bring", "wednesday"]

## `POST`

Passing this JSON:

```js
{"count": 6}
```

[With curl](https://stackoverflow.com/a/7173011/6591491):

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"count": 6}' \
  https://us-central1-omega-functions.cloudfunctions.net/random-words
```

May return:

> ["winds", "frankfurt", "instructors", "text", "stem", "start"]
