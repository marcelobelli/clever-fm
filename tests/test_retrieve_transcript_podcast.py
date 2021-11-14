from helpers import retrieve_transcript_podcast


def test_function():
    transcript_path = "./fixture-ep-1.txt"
    expected = [
        "0:01  ",
        "When I was a kid, apples were garbage. They were called Red Delicious and they were red. They were not delicious. They looked beautiful, but then you bite into it, and almost always it would be mushy and mealy, just nasty.",
        "",
        "0:15  ",
        "It was a really bad time to be an apple eater. It was also a really bad time to be an apple grower.",
        "",
        "0:21  ",
        "Everybody really just about literally everybody was growing Red Delicious.",
        "",
        "0:24",
        "And I'm Dan Charles. Thanks for listening.",
        "",
        "Transcribed by https://otter.ai",
        "",
    ]

    assert retrieve_transcript_podcast(transcript_path) == expected
