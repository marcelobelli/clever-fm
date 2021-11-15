from dataclasses import dataclass
from typing import Optional

import helpers


@dataclass
class Transcript:
    _data: list

    def __getitem__(self, position):
        return self._data[position]

    def get_excerpt(self, start_time: int, end_time: Optional[int]) -> str:
        start_time = start_time if start_time > 0 else 1
        end_time = end_time if end_time else len(self._data)
        excerpt = [word for word in helpers.flatten_iterables(self._data[start_time:end_time])]

        return " ".join(excerpt)

    @classmethod
    def create_from_transcript_data(cls, transcript_data: list[str]) -> "Transcript":
        transcript = cls(_data=[""])

        for excerpt in helpers.raw_transcript_to_excerpts(transcript_data):
            for words in helpers.words_per_second_from_excerpt(excerpt):
                transcript._data.append(words)

        return transcript
