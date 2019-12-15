from hypothesis import given
import hypothesis.strategies as st
import hypothesis.extra.numpy as hnp
import numpy as np
import linear


from linear import SolveGaussSeidel, SolveSOR, CheckDiagDominant,MakeItDiagDominant

@given( l= hnp.arrays(np.float, (3,3), elements=st.floats(1,10)))
def test_diag_dominant(l):
    #print("inside test.")
    print(l)
    assert CheckDiagDominant(MakeItDiagDominant(l)) == True

# @given( l= hnp.arrays(np.float, (2,3), elements=st.floats(1,2)))
# def test_SolveGaussSeidel(l):

#     pass    



# @given(st=text())
# @example([])
# def test_SolveSOR(s):
#     pass
if __name__ == "__main__":
    test_diag_dominant()