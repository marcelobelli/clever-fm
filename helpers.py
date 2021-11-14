from collections import Counter

from exceptions import TimestampFormatException


def timestamp_to_seconds(timestamp: str) -> int:
    c = Counter(timestamp)

    match c[":"]:
        case 1:
            hours, minutes, seconds = 0, *timestamp.split(":")

        case 2:
            hours, minutes, seconds = timestamp.split(":")

        case _:
            raise TimestampFormatException

    try:
        hours = int(hours)
        minutes = int(minutes)
        seconds = int(seconds)
    except ValueError:
        raise TimestampFormatException

    return hours * 3600 + minutes * 60 + seconds


def retrieve_transcript_podcast(transcript_path: str) -> list[str]:
    with open(transcript_path, "r") as file:
        text = file.read()

    lines = text.split("\n")
    return lines
