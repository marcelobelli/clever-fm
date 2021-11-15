from pydantic import BaseModel

import helpers


class Transcript(BaseModel):
    _data: list = [""]

    def __getitem__(self, position):
        return self._data[position]


    @classmethod
    def create_from_transcript_data(cls, transcript_data: list[str]) -> "Transcript":
        transcript = cls()

        for excerpt in helpers.raw_transcript_to_excerpts(transcript_data):
            for words in helpers.words_per_second_from_excerpt(excerpt):
                transcript._data.append(words)

        return transcript
