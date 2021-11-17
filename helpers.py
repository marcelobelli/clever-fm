from collections import Counter
from typing import Iterable, Iterator, Union

from exceptions import TimestampFormatException
from math import floor

RANGE_IN_SECS_FALLBACK = 3


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
        range_in_secs = excerpt[2] - excerpt[0]
    except TypeError:
        range_in_secs = RANGE_IN_SECS_FALLBACK

    words = excerpt[1].split(" ")
    total_words = len(words)
    words_per_sec = floor(total_words / range_in_secs)

    initial = 0
    end = words_per_sec
    diff = total_words % range_in_secs

    for i in range(range_in_secs):
        if diff > 0:
            end += 1
            diff -= 1
        yield " ".join(words[initial:end])
        initial = end
        end += words_per_sec
