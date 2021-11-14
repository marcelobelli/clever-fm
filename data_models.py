from dataclasses import dataclass
from typing import Iterator, Optional

from exceptions import TimestampFormatException
from helpers import timestamp_to_seconds


@dataclass
class Transcript:
    pass

    @classmethod
    def raw_transcript_to_excerpts(cls, raw_transcript: list[str]) -> Iterator[list[int, str, Optional[int]]]:
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
