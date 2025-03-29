import pytest

def add(a, b):
    return a + b

def add_numbers(number_list):
    return sum(number_list)

def capitalize_words(text):
    return text.title()

def test_add():
    assert add(1, 2) == 3, "Komunikat błędu"
    assert add(-1, 1) == 0, "Komunikat błędu"
    assert add(-1, -1) == -2

@pytest.fixture
def number_list():
    return [1, 2, 3, 4, 5]

def test_add_numbers(number_list):
    assert add_numbers(number_list) == 15, f"Lista: {number_list}"

@pytest.mark.parametrize("input_text,expected", [
    ("hello world", "Hello World"),
    ("python test", "Python Test"),
    ("a b c", "A B C"),
    ("", ""),
    ("already Capitalized", "Already Capitalized")
])
def test_capitalize_words(input_text, expected):
    result = capitalize_words(input_text)
    assert result == expected