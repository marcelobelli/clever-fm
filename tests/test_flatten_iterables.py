from helpers import flatten_iterables


def test_flatten_iterables():
    iterable = [["When", "I", "was"], ["a", "kid,", "apples"], ["were", "garbage.", "They"]]
    expected = ["When", "I", "was", "a", "kid,", "apples", "were", "garbage.", "They"]

    assert list(flatten_iterables(iterable)) == expected
