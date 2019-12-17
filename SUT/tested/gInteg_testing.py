from hypothesis import given,example
import hypothesis.strategies as st
import numpy as np

from gInteg import Integration_GaussLegendre, calculate, solve,get_param


@given(n = st.floats(1.0,5.0), flg = st.booleans())
@example(1.0,True)
def test_calculate(n,flg):
    f = "1/(x**2+4)"
    result = calculate(f,n,flg)
    x = 0
    y = 0
    if flg:
        x = 1/n
        y = eval(f) *(-1/(n*n))
    else:
        x = n
        y = eval(f)


    assert isinstance(result, float)
    assert result == y

@given(n = st.integers(1,10))
@example(2)
def test_get_param(n):
    if n != 2 and n !=3:
        assert get_param(n) == "error"
    else:
        w,x = get_param(n)
        assert len(w) != 0

    

@given(n = st.floats(1.0,5.0), a = st.floats(1.0,5.0), b = st.floats(1.0,5.0))
@example(2,2,1e9)
def test_Integration_GaussLegendre(n,a,b):
    f = "1/(x**2+4)"
    result = Integration_GaussLegendre(f,n,a,b)
    assert isinstance(result,float)


if __name__=="__main__":
    test_get_param()
    test_calculate()
    test_Integration_GaussLegendre()