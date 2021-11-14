from collections import Counter


def timestamp_to_seconds(timestamp: str) -> int:
    c = Counter(timestamp)

    match c[":"]:
        case 1:
            hours, minutes, seconds = 0, *timestamp.split(":")

        case 2:
            hours, minutes, seconds = timestamp.split(":")

    return int(hours) * 3600 + int(minutes) * 60 + int(seconds)
