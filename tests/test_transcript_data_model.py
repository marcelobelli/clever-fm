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
        (15, ["It", "was", "a", "really"]),
        (16, ["bad", "time", "to", "be"]),
        (17, ["an", "apple", "eater.", "It"]),
        (18, ["was", "also", "a", "really"]),
        (19, ["bad", "time", "to", "be"]),
        (20, ["an", "apple", "grower."]),
        (21, ["Everybody", "really", "just"]),
        (22, ["about", "literally", "everybody"]),
        (23, ["was", "growing", "Red"]),
        (24, ["Delicious."]),
        (24, ["And", "I'm"]),
        (25, ["Dan", "Charles."]),
        (26, ["Thanks", "for"]),
        (27, ["listening."]),
    ]

    transcript = Transcript.create_from_transcript_data(transcript_data)

    assert transcript._data == expected


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
