import pytest

from data_models import Transcript


@pytest.fixture
def raw_transcript():
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


def test_transform_raw_transcript_into_clean_full_excerpts(raw_transcript):
    expected = [
        [
            1,
            "When I was a kid, apples were garbage. They were called Red Delicious and they were red. They were not delicious. They looked beautiful, but then you bite into it, and almost always it would be mushy and mealy, just nasty.",
            15,
        ],
        [15, "It was a really bad time to be an apple eater. It was also a really bad time to be an apple grower.", 21],
        [21, "Everybody really just about literally everybody was growing Red Delicious.", 24],
        [24, "And I'm Dan Charles. Thanks for listening.", None],
    ]
    excerpts = [excerpt for excerpt in Transcript.raw_transcript_to_excerpts(raw_transcript)]

    assert excerpts == expected
