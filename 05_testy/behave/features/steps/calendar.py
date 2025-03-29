from behave import *

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

@given('The year {year:d}')
def step_impl(context, year):
    context.year = year
    context.is_leap_year = is_leap_year(year)

@then('it should return {is_leap_year}')
def step_impl(context, is_leap_year):
    is_leap_year = bool(is_leap_year.lower() == "true")
    assert context.is_leap_year == is_leap_year
