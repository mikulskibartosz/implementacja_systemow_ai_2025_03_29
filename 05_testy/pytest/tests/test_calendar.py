# Rok przestępny = podzielny przez 4, ale nie podzielny przez 100, chyba że jest podzielny przez 400

# zwykły
# podzielny przez 4
# nie podzielny przez 100
# podzielny przez 400
# rok 0 nie istnieje

import pytest

def is_leap_year(year):
    if year == 0:
        raise ValueError("Rok 0 nie istnieje")
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True
    return False


def test_regular_year():
    assert is_leap_year(2001) == False
    assert is_leap_year(2002) == False
    assert is_leap_year(2003) == False

def test_div_4():
    assert is_leap_year(2004) == True
    assert is_leap_year(2008) == True
    assert is_leap_year(2012) == True

def test_div_100():
    assert is_leap_year(1900) == False
    assert is_leap_year(2100) == False

def test_div_400():
    assert is_leap_year(2000) == True
    assert is_leap_year(2400) == True

def test_year_0():
    with pytest.raises(ValueError):
        is_leap_year(0)
