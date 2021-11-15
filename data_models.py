from dataclasses import dataclass
from typing import Iterator

from exceptions import TimestampFormatException
from helpers import timestamp_to_seconds

TIME_RANGE_FALLBACK = 3


@dataclass
class Transcript:
    pass

    @classmethod
    def words_per_second_from_excerpt(cls, excerpt: list) -> Iterator[tuple[int, list[str]]]:
        try:
            time_range = excerpt[2] - excerpt[0]
        except TypeError:
            time_range = TIME_RANGE_FALLBACK
        words = excerpt[1].split(" ")
        words_per_sec = round(len(words) / time_range)

        for i in range(0, len(words), words_per_sec):
            yield words[i : i + words_per_sec]

    @classmethod
    def raw_transcript_to_excerpts(cls, raw_transcript: list[str]) -> Iterator[list]:
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
