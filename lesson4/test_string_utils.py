import pytest
from string_utils import StringUtils


utils = StringUtils()


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("тест", "Тест"),
        ("123", "123"),
        ("04 апреля 2023", "04 апреля 2023"),
    ],
)
def test_capitalize_positive(inp, expected):
    assert utils.capitalize(inp) == expected


@pytest.mark.parametrize(
    "inp",
    [
        "",
        " ",
    ],
)
def test_capitalize_negative_empty_and_space(inp):
    assert utils.capitalize(inp) == inp


@pytest.mark.parametrize(
    "inp, expected",
    [
        ("   тест", "тест"),
        ("тест", "тест"),
        ("   123", "123"),
        ("   04 апреля 2023", "04 апреля 2023"),
    ],
)
def test_trim_positive(inp, expected):
    assert utils.trim(inp) == expected


def test_trim_empty_string():
    assert utils.trim("") == ""


def test_trim_space_only():
    assert utils.trim("   ") == ""


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "S", True),
        ("SkyPro", "U", False),
        ("123", "2", True),
        ("04 апреля 2023", " ", True),
    ],
)
def test_contains_positive(string, symbol, expected):
    assert utils.contains(string, symbol) == expected


@pytest.mark.parametrize(
    "string, symbol",
    [
        ("", "a"),
        (" ", "a"),
    ],
)
def test_contains_negative(string, symbol):
    assert utils.contains(string, symbol) is False


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("SkyPro", "k", "SyPro"),
        ("SkyPro", "Pro", "Sky"),
        ("123123", "1", "2323"),
        ("04 апреля 2023", " ", "04апреля2023"),
    ],
)
def test_delete_symbol_positive(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected


@pytest.mark.parametrize(
    "string, symbol, expected",
    [
        ("", "a", ""),
        (" ", "a", " "),
    ],
)
def test_delete_symbol_negative(string, symbol, expected):
    assert utils.delete_symbol(string, symbol) == expected
