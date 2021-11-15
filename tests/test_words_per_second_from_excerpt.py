from helpers import words_per_second_from_excerpt


def test_get_words_per_second_from_excerpt_with_initial_and_end_timestamp():
    excerpt = [
        1,
        "When I was a kid, apples were garbage. They were called Red Delicious and they were red. They were not delicious. They looked beautiful, but then you bite into it, and almost always it would be mushy and mealy, just nasty.",
        15,
    ]
    expected = [
        (1, ["When", "I", "was"]),
        (2, ["a", "kid,", "apples"]),
        (3, ["were", "garbage.", "They"]),
        (4, ["were", "called", "Red"]),
        (5, ["Delicious", "and", "they"]),
        (6, ["were", "red.", "They"]),
        (7, ["were", "not", "delicious."]),
        (8, ["They", "looked", "beautiful,"]),
        (9, ["but", "then", "you"]),
        (10, ["bite", "into", "it,"]),
        (11, ["and", "almost", "always"]),
        (12, ["it", "would", "be"]),
        (13, ["mushy", "and", "mealy,"]),
        (14, ["just", "nasty."]),
    ]
    result = [r for r in words_per_second_from_excerpt(excerpt)]

    assert result == expected


def test_get_words_per_second_from_excerpt_from_the_middle_of_the_transcript():
    excerpt = [
        15,
        "It was a really bad time to be an apple eater. It was also a really bad time to be an apple grower.",
        21,
    ]
    expected = [
        (15, ["It", "was", "a", "really"]),
        (16, ["bad", "time", "to", "be"]),
        (17, ["an", "apple", "eater.", "It"]),
        (18, ["was", "also", "a", "really"]),
        (19, ["bad", "time", "to", "be"]),
        (20, ["an", "apple", "grower."]),
    ]

    result = [r for r in words_per_second_from_excerpt(excerpt)]

    assert result == expected


def test_get_words_per_second_from_excerpt_when_ending_is_none():
    excerpt = [24, "And I'm Dan Charles. Thanks for listening.", None]
    expected = [(24, ["And", "I'm"]), (25, ["Dan", "Charles."]), (26, ["Thanks", "for"]), (27, ["listening."])]

    result = [r for r in words_per_second_from_excerpt(excerpt)]

    assert result == expected
