from hypothesis import given, assume,seed,settings,HealthCheck
import hypothesis.strategies as st
import hypothesis.extra.numpy as hnp
import numpy as np
# import hypothesis

from curve import curve_fitting

def fun1(x):
    return x ** 4 + x ** 3 + x ** 2 + x  ** 1 +6565656

# x = list(range(100))
# y = list(map(fun1, x))
# actual = curve_fitting(x,y,degree=4)
# expected =np.polyfit(x, y, 4)
# print(actual)
# print(expected)
# for i in range(len(actual)):
#     print(i,actual[i]==expected[i])
# if actual.all() == expected.all():
#     print("eeh")

# a = 3.4536
# b="{0:.1f}".format(a)
# print(b)

#hnp.array_shapes(min_dims=1,max_dims=1) # shapeeeee -->
# @given(x=hnp.arrays(np.integer,st.integers(1,20),elements=st.integers(1,100),unique=True),y=hnp.arrays(np.integer,st.integers(1,20),elements=st.integers(1,100),unique=True))
# @seed(223990654631554444241352763141105284211)
# HealthCheck.filter_too_much,
@settings(suppress_health_check=(HealthCheck.filter_too_much,HealthCheck.too_slow,))
@given(m=hnp.arrays(np.integer,hnp.array_shapes(min_dims=2,max_dims=2,min_side=2, max_side=10),elements=st.integers(1,100),unique=True))
# @example([])
def test_curve_fitting(m):
    assume(m.shape[0]==2) # i want 2 vectors only
    # assume(np.linalg.matrix_rank(np.dot(m[0],m[0].T)) == m.shape[1] )
    # print(x)
    x = m[0]
    y = m[1]
    deg = m.shape[1]
    k=np.dot(x,x.T)
    # k=np.matmul(np.dot(x,x.T), y) # k has to be singular
    print(x)
    actual = curve_fitting(x,y,deg)
    # assume(np.linalg.matrix_rank(k) == deg )
    if np.linalg.matrix_rank(k) == deg:    
        expected =np.polyfit(x, y, deg)
        assert expected.all()==actual.all()
    else:
        expected = 0 
        assert actual.all() == expected
         
    
    # print(k)
    # print(x.shape)

    #assume(len(x)==len(y))
    # print(len(x), len(y))
    # pass    



test_curve_fitting()