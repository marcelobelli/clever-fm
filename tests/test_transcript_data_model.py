import pytest

from data_models import Transcript


@pytest.fixture
def transcript_data():
    return [
        "0:01  ",
        "When I was a kid, apples were garbage. They were called Red Delicious and they were red. They were not delicious. They looked beautiful, but then you bite into it, and almost always it would be mushy and mealy, just nasty.",
        "",
        "0:15  ",
        "It was a really bad time to be an apple eater. It was also a really bad time to be an apple grower.",
        "",
        "0:21  ",
        "Everybody really just about literally everybody was growing Red Delicious.",
        "",
        "0:24",
        "And I'm Dan Charles. Thanks for listening.",
        "",
        "Transcribed by https://otter.ai",
        "",
    ]


@pytest.fixture
def transcript(transcript_data):
    return Transcript.create_from_transcript_data(transcript_data)


def test_create_transcript_dataclass_from_transcript_data(transcript_data):
    expected = [
        "",
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
        ["It", "was", "a", "really"],
        ["bad", "time", "to", "be"],
        ["an", "apple", "eater.", "It"],
        ["was", "also", "a", "really"],
        ["bad", "time", "to", "be"],
        ["an", "apple", "grower."],
        ["Everybody", "really", "just"],
        ["about", "literally", "everybody"],
        ["was", "growing", "Red"],
        ["Delicious."],
        ["And", "I'm"],
        ["Dan", "Charles."],
        ["Thanks", "for"],
        ["listening."],
    ]

    transcript = Transcript.create_from_transcript_data(transcript_data)

    assert transcript._data == expected


@pytest.mark.parametrize(
    "cut, expected_result",
    (
        (slice(1, 2), [["When", "I", "was"]]),
        (slice(2, 5), [["a", "kid,", "apples"], ["were", "garbage.", "They"], ["were", "called", "Red"]]),
    ),
)
def test_get_on_transcript(cut, expected_result, transcript):
    assert transcript[cut] == expected_result


@pytest.mark.parametrize(
    "start_time, end_time, expected",
    (
        (0, 3, "When I was a kid, apples were garbage. They"),
        (1, 3, "When I was a kid, apples were garbage. They"),
        (3, 3, "were garbage. They"),
        (5, 7, "Delicious and they were red. They were not delicious."),
        (25, None, "And I'm Dan Charles. Thanks for listening."),
    ),
)
def test_get_excerpt(start_time, end_time, expected, transcript):
    assert transcript.get_excerpt(start_time, end_time) == expected
