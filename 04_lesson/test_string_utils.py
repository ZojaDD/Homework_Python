import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    ("   Skypro", "Skypro"),
    (" hello world", "hello world"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("   123abc", "123abc"),
    ("   ", ""),
    ("   .", "."),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("SkyPro", "S", "True"),
    ("Skypro", "h", "False"),
    ("hello world", "w", "True"),
])
def test_contains_positive(input_str, input_symbol, expected):
    assert string_utils.contains(input_str) == expected


@pytest.mark.parametrize("input_str, input_symbol, expected", [
    ("", "f", "False"),
    ("   ", "k", "False"),
    ("   .", ".", "True"),
])
def test_contains_negative(input_str, input_symbol, expected):
    assert string_utils.contains(input_str) == expected


@pytest.mark.parametrize("input_string, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("hello world", " world", "hello"),
])
def test_delete_symbol_positive(input_string, input_symbol, expected):
    assert string_utils.delete_symbol(input_string) == expected


@pytest.mark.parametrize("input_string, input_symbol, expected", [
    ("SkyPro", "", "SkyPro"),
    ("SkyPro", "v", "SkyPro"),
    ("   ", "a", "   "),
])
def test_delete_symbol_negative(input_string, input_symbol, expected):
    assert string_utils.delete_symbol(input_string) == expected
