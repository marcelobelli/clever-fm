from helpers import timestamp_to_seconds


def test_conversion_when_has_minutes_and_seconds():
    timestamp = "8:38"
    expected = 518

    assert timestamp_to_seconds(timestamp) == expected


def test_conversion_when_has_hours_minutes_and_seconds():
    timestamp = "1:10:06"
    expected = 4206

    assert timestamp_to_seconds(timestamp) == expected