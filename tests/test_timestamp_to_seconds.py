import pytest

from exceptions import TimestampFormatException
from helpers import timestamp_to_seconds


def test_conversion_when_has_minutes_and_seconds():
    timestamp = "8:38"
    expected = 518

    assert timestamp_to_seconds(timestamp) == expected


def test_conversion_when_has_hours_minutes_and_seconds():
    timestamp = "1:10:06"
    expected = 4206

    assert timestamp_to_seconds(timestamp) == expected


@pytest.mark.parametrize(
    "bad_input", ("1::0", "Transcribed by https://otter.ai", "Lorem Ipsum", "2021-11-14 17:27:07.208146", None)
)
def test_when_someone_sends_a_bad_input_to_the_function(bad_input):
    with pytest.raises(TimestampFormatException):
        timestamp_to_seconds(bad_input)
