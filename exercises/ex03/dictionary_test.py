"""Defining test functions"""

__author__ = "730719749"

from dictionary import invert, favorite_color, count, bin_len
import pytest


def test_invert_dupe_key() -> None:
    with pytest.raises(KeyError):
        my_dictionary = {"kris": "jordan", "michael": "jordan"}
        invert(my_dictionary)


def test_invert_1() -> None:
    assert {"no": "yo", "hi": "yes"} == invert({"yo": "no", "yes": "hi"})


def test_invert_2() -> None:
    assert {"jon": "claire", "eleni": "jas"} == invert(
        {"claire": "jon", "jas": "eleni"}
    )


def test_count_edge() -> None:
    assert count([]) == {}


def test_count() -> None:
    assert count(["Jasmine", "Jordan", "Jonathan", "Jordan"]) == {
        "Jasmine": 1,
        "Jordan": 2,
        "Jonthan": 1,
    }


def test_count_1() -> None:
    assert count(["Jasmine", "Jordan", "Jonathan"]) == {
        "Jasmine": 1,
        "Jordan": 1,
        "Jonthan": 1,
    }


def test_fav_color_edge() -> None:
    assert favorite_color({"Eleni": "Red", "Jon": "Blue"}) == "Red"


def test_fav_color_1() -> None:
    assert favorite_color({"Eleni": "Red", "Jon": "Blue", "Bob": "Red"}) == "Red"


def test_fav_color_2() -> None:
    assert (
        favorite_color(
            {"Eleni": "Red", "Jon": "Blue", "Bob": "Green", "Claire": "Blue"}
        )
        == "Blue"
    )


def test_bin_len_edge() -> None:
    assert bin_len({"", "", ""}) == {0: {""}}


def test_bin_1() -> None:
    assert bin_len(["the", "quick", "fox"]) == {3: {"the", "fox"}, 5: {"quick"}}


def test_bin_2() -> None:
    assert bin_len(["the", "the", "fox"]) == {3: {"the", "fox"}}
