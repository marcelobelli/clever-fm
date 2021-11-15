from collections import Counter
from typing import Iterable, Iterator, Union

from exceptions import TimestampFormatException

TIME_RANGE_FALLBACK = 3


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


def raw_transcript_to_excerpts(raw_transcript: list[str]) -> Iterator[list]:
    timestamp = timestamp_to_seconds(raw_transcript[0])
    excerpt = [timestamp]

    for i in range(3, len(raw_transcript), 3):
        excerpt.append(raw_transcript[i - 2])

        try:
            timestamp = timestamp_to_seconds(raw_transcript[i])
        except TimestampFormatException:
            excerpt.append(None)
        else:
            excerpt.append(timestamp)

        if len(excerpt) == 3:
            yield excerpt
            excerpt = [timestamp]


def words_per_second_from_excerpt(excerpt: list) -> Iterator[tuple[int, list[str]]]:
    try:
        time_range = excerpt[2] - excerpt[0]
    except TypeError:
        time_range = TIME_RANGE_FALLBACK
    words = excerpt[1].split(" ")
    words_per_sec = round(len(words) / time_range)
    second = excerpt[0]

    for i in range(0, len(words), words_per_sec):
        yield second, words[i : i + words_per_sec]
        second += 1


def flatten_iterables(value: Union[Iterable, str]):
    if isinstance(value, str):
        yield value
    else:
        for x in value:
            if not isinstance(x, Iterable):
                continue
            yield from flatten_iterables(x)
