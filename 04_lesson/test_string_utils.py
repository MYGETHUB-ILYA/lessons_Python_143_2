import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# позитивное тестирование всех функций ---------------------------------------
# capitalize


@pytest.mark.positive_test
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
    ("WORLD", "World"),
    ("ФSУвыFGмпа", "Фsувыfgмпа"),
    ("a", "A"),
    ("abCdEfg", "Abcdefg"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# trim


@pytest.mark.parametrize("input_str, expected", [
    ("Sparrow", "Sparrow"),
    (" Sparrow", "Sparrow"),
    ("     Sparrow", "Sparrow"),
    ("     sparrow", "sparrow"),
    ("     sparRoW", "sparRoW"),
    (" всего два слова", "всего два слова"),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected

# contains


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("QWERTY", "R", True),
    ("йцукен", "й", True),
    ("qwerty/&12", "/", True),
    ("qwerty/&12", "1", True),
    ("всего три слова", "лов", True),
    ("qwerty", "qwerty", True),
    ("qwerty", "", True),
    ("  ", "  ", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


# delete_symbol
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("молоко", "о", "млк"),
    ("cсcсcсcсcсcсcсcсcс", "c", "ссссссссс"),
    ("MМMМMМMМMМMМMМMМMМMМMМ", "М", "MMMMMMMMMMM"),
    ("Нужно удалить все эти буквы", "у", "Нжно далить все эти бквы"),
    ("если начать проверку нескольких букв на час",
     "ча", "если нать проверку нескольких букв на с"),
    ("удалить все", "удалить все", ""),
    ("11111111", "11", ""),
    ("aaaabbbbcccccccc", "bb", "aaaacccccccc"),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected

# negative ---------------------------------------------------------------
# capitalize negative


@pytest.mark.negative_test
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
    (" world", " world"),
    ("/-+вк32а", "/-+вк32а")
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

# trim negative


@pytest.mark.parametrize("input_str, expected", [
    (" s p a r R o W", "s p a r R o W"),
    ("1 2sparRoW", "1 2sparRoW"),
    (" 1 2sparRoW", "1 2sparRoW"),
    ("  ab", "ab"),
    ("     ", ""),
    ("", ""),
    (" всего два слова  ", "всего два слова  "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected

# contains


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("QWERTY", "a", False),
    ("qwerty", "Q", False),
    ("qwerty", "ytrewq", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

# delete_symbol


@pytest.mark.parametrize("input_str, symbol, expected", [
    ("", "abc", ""),
    ("удалить все", "удалитьвсе", "удалить все"),
    ("Удаление", "удалениЕ", "Удаление"),
    ("ффффффффффффф", "фф", "ф"),
    ("фффффффффффф", "ффф", ""),
    ("aaaabbbbcccccccc", "bb", "aaaacccccccc")
])
def test_delete_symbol_negative(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected
