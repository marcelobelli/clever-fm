from helpers import words_per_second_from_excerpt


def test_get_words_per_second_from_excerpt_with_initial_and_end_timestamp():
    excerpt = [
        1,
        "When I was a kid, apples were garbage. They were called Red Delicious and they were red. They were not delicious. They looked beautiful, but then you bite into it, and almost always it would be mushy and mealy, just nasty.",
        15,
    ]
    expected = [
        ["When", "I", "was"],
        ["a", "kid,", "apples"],
        ["were", "garbage.", "They"],
        ["were", "called", "Red"],
        ["Delicious", "and", "they"],
        ["were", "red.", "They"],
        ["were", "not", "delicious."],
        ["They", "looked", "beautiful,"],
        ["but", "then", "you"],
        ["bite", "into", "it,"],
        ["and", "almost", "always"],
        ["it", "would", "be"],
        ["mushy", "and", "mealy,"],
        ["just", "nasty."],
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
        ["It", "was", "a", "really"],
        ["bad", "time", "to", "be"],
        ["an", "apple", "eater.", "It"],
        ["was", "also", "a", "really"],
        ["bad", "time", "to", "be"],
        ["an", "apple", "grower."],
    ]

    result = [r for r in words_per_second_from_excerpt(excerpt)]

    assert result == expected


def test_get_words_per_second_from_excerpt_when_ending_is_none():
    excerpt = [24, "And I'm Dan Charles. Thanks for listening.", None]
    expected = [["And", "I'm"], ["Dan", "Charles."], ["Thanks", "for"], ["listening."]]

    result = [r for r in words_per_second_from_excerpt(excerpt)]

    assert result == expected
