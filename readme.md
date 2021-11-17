# Clever.fm: Take Home Problem

### Data Structure

For the transcript, the `list` data structure was my choice from the beginning.

#### Why

My idea was to use the index as a reference of second of the transcript. 
With that, I could retrieve any segment of the transcript in O(1).

### Challenges

Make the `words_per_second_from_excerpt` function wo[rks correctly. It was hard to find
the "sweet spot" to make the right division in a way that the function would always
distribute words respecting the number of seconds that each segment has.

### Known Issues

The flow to transform the transcript **text** into a transcript **object** is not very performatic.
But at the same time I think that in a real world scenario this transformation would only occur once,
so maybe it's the kind of thing that could run until we need to escalate.

### Tests

To run the tests that I create, first install pytest

```shell
$ pip install -r requirements-dev.txt
```

Then run pytest

```shell
$ pytest
```
