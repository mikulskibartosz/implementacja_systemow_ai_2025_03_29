from hypothesis import given, example, settings, strategies as st

def reverse_list(lst):
    return lst[::-1]

@given(st.lists(st.integers(min_value=0, max_value=100)))
@example([1, 2, 3, 4, 5])
@settings(max_examples=1000)
def test_reverse_twice_is_identity(lst):
    """Test czy podwójne odwrócenie listy = tożsamość."""
    assert reverse_list(reverse_list(lst)) == lst