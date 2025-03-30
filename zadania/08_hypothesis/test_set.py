from hypothesis import given, strategies as st


@given(st.sets(st.integers()))
def test_adding_existing_element_does_not_change_set(s):
    """Test that adding an existing element does not change the set."""
    if not s:
        return

    element = next(iter(s))
    original_size = len(s)
    s.add(element)
    assert len(s) == original_size


@given(st.sets(st.integers()), st.integers())
def test_adding_new_element_increases_set_by_one(s, element):
    """Test that adding a new element increases the set size by 1."""
    if element in s:
        return

    original_size = len(s)
    s.add(element)
    assert len(s) == original_size + 1


@given(st.sets(st.integers()))
def test_union_with_empty_set_does_not_change_set(s):
    """Test that union with an empty set does not change the set."""
    empty_set = set()
    result = s.union(empty_set)
    assert result == s


@given(st.sets(st.integers()))
def test_union_with_itself_does_not_change_set(s):
    """Test that union with itself does not change the set."""
    result = s.union(s)
    assert result == s


@given(st.sets(st.integers()), st.sets(st.integers()))
def test_union_commutativity(s1, s2):
    """Test that union operation is commutative: A ∪ B = B ∪ A."""
    assert s1.union(s2) == s2.union(s1)


@given(st.sets(st.integers()), st.sets(st.integers()), st.sets(st.integers()))
def test_union_associativity(s1, s2, s3):
    """Test that union operation is associative: (A ∪ B) ∪ C = A ∪ (B ∪ C)."""
    assert s1.union(s2).union(s3) == s1.union(s2.union(s3))
