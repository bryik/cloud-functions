# hello-world

This function echoes back any message passed to it. If no message is passed, it responds with "Hello world!".

**Endpoint:** https://us-central1-omega-functions.cloudfunctions.net/hello-world

## Hello

To see "Hello world!", a simple `GET` will suffice:

```bash
curl -g https://us-central1-omega-functions.cloudfunctions.net/hello-world
```

Will return:

> Hello World!

## Echo

To get the function to echo back your message, either make a `GET` request with a 'message' query parameter or `POST` a JSON with a "message" property.

### `GET`

```bash
curl -g https://us-central1-omega-functions.cloudfunctions.net/hello-world?message=echoooo!
```

Will return:

> echoooo!

### `POST`

For example, pass this JSON:

```js
{"message": "echooooo!"}
```

[Using curl](https://stackoverflow.com/a/7173011/6591491):

```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"message": "echooooo!"}' \
  https://us-central1-omega-functions.cloudfunctions.net/hello-world
```

Will return:

> echoooo!

## Reference

I did not write this function. It is the default example Google supplies when you create a new cloud function [on their platform](https://cloud.google.com/functions/).
