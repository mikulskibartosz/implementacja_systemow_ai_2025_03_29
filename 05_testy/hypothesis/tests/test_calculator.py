from hypothesis import given, strategies as st

@given(st.integers())
def test_adding_zero_is_identity(a):
    assert a + 0 == a

@given(st.integers(), st.integers())
def test_add_is_commutative(a, b):
    assert a + b == b + a

@given(st.integers(), st.integers(), st.integers())
def test_add_is_associative(a, b, c):
    assert a + (b + c) == (a + b) + c

