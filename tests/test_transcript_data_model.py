import pytest

from data_models import Transcript
from helpers import retrieve_transcript_podcast


@pytest.fixture
def transcript_data(episode_1_file):
    return retrieve_transcript_podcast(episode_1_file)


@pytest.fixture
def transcript(transcript_data):
    return Transcript.create_from_transcript_data(transcript_data)


def test_create_transcript_dataclass_from_transcript_data(transcript_data):
    transcript = Transcript.create_from_transcript_data(transcript_data)

    assert len(transcript._data) > 0


@pytest.mark.parametrize(
    "start_time, end_time, expected",
    (
        (
            0,
            15,
            "When I was a kid, apples were garbage. They were called Red Delicious and they were red. They were not delicious. They looked beautiful, but then you bite into it, and almost always it would be mushy and mealy, just nasty.",
        ),
        (
            1,
            15,
            "When I was a kid, apples were garbage. They were called Red Delicious and they were red. They were not delicious. They looked beautiful, but then you bite into it, and almost always it would be mushy and mealy, just nasty.",
        ),
        (1, 4, "When I was a kid, apples were garbage. They"),
        (3, 3, ""),
        (5, 8, "Delicious and they were red. They were not delicious."),
        (21, 24, "Everybody really just about literally everybody was growing Red Delicious."),
        (480, 484, "when the honeycrisp finally get to the store, they do great"),
        (480, 482, "when the honeycrisp finally get to"),
        (
            801,
            None,
            "was produced by Jess Jang and Neda Wilson. And finally, if you're looking for another great podcast, check out snap judgment with Glenn Washington. It's an hour long show of real stories about real people. You can find it on the NPR one. I'm Jacob Goldstein. And I'm Dan Charles. Thanks for listening.",
        ),
    ),
)
def test_get_excerpt(start_time, end_time, expected, transcript):
    assert transcript.get_excerpt(start_time, end_time) == expected


def test_create_episodes_data(episode_1_file, episode_2_file, episode_3_file):
    episodes = [episode_1_file, episode_2_file, episode_3_file]
    expected_episodes_id = ["fixture-ep-1", "fixture-ep-2", "fixture-ep-3"]

    episodes_data = Transcript.create_episodes_data(episodes)

    assert list(episodes_data.keys()) == expected_episodes_id

    for transcript in episodes_data.values():
        assert isinstance(transcript, Transcript)
