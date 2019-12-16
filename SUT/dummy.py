# from hypothesis import given, strategies as st
# @given(st.integers().filter(lambda x: x % 2 == 0))
# def test_even_integers(i):
#     pass
from hypothesis import given, event, strategies as st


@given(st.integers().filter(lambda x: x % 2 == 0))
def test_even_integers(i):
    event("i mod 3 = %d" % (i % 3,))