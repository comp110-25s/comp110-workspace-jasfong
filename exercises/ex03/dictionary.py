"""Dictionary Functions"""

__author__ = "730719749"


def invert(start: dict[str, str]) -> dict[str, str]:
    """Take a Dictionary and return keys/values inverted"""
    flipped: dict[str, str] = {}
    for key in start:
        value = start[key]

        if value in flipped:
            raise KeyError("Error, already in the key.")
        else:
            flipped[value] = key
    return flipped


def count(frequency: list[str]) -> dict[str, int]:
    """Count # of times value appears in list and return a dict"""
    results: dict[str, int] = {}
    for i in frequency:
        if i in results:
            results[i] += 1
        else:
            results[i] = 1
    return results


def favorite_color(colors: dict[str, str]) -> str:
    """Finds the most popular fav color based on frequency"""
    count: dict[str, int] = {}
    key_list: list[str] = []
    for key in colors:
        if colors[key] not in key_list:
            count[colors[key]] = 1
            key_list.append(colors[key])
        else:
            count[colors[key]] += 1
    max_count: int = 0
    max_color: str = ""
    for key in count:
        if count[key] > max_count:
            max_count = count[key]
            max_color = key
    return max_color


def bin_len(list: list[str]) -> dict[int, set[str]]:
    bins: dict[int, set[str]] = {}

    for word in list:
        length = len(word)
        if length not in bins:
            bins[length] = set()
            bins[length].add(word)
        else:
            bins[length].add(word)
    return bins
