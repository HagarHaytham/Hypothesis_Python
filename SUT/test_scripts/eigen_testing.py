from hypothesis import given , assume , note
import hypothesis.strategies as st
import numpy as np
import hypothesis.extra.numpy as numpy
from numpy import linalg as linear
from tested.eigen import powerMethod, deflate

@st.composite
def generate_data(draw):
    
    
    dim = draw( st.integers(min_value = 3 , max_value = 10) )
    
    matrix_under_test= draw(numpy.arrays(dtype=np.integer,shape=(dim,dim), elements=st.integers(1,10),unique = True))
    
    
    
    return matrix_under_test

@given(matrix_under_test = generate_data())
def test_power_method(matrix_under_test):
    try:
        eigen_value , eigen_vector , error = powerMethod(matrix_under_test)
    except:
        pass
    numpy_eigen_values , numpy_eigen_vectors = linear.eig(matrix_under_test)
    note(" eigen value diff %r"%  abs(numpy_eigen_values[0]-eigen_value))
    note("error  %r"% error)
    assert abs(numpy_eigen_values[0] - eigen_value) <= error 
    i= 0
    for eigen_vector_value in numpy_eigen_vectors[0]:
        note(" eigen vector value diff %r"% abs(eigen_vector_value-eigen_vector[i]))
        note("error  %r"% error)
        assert  abs(eigen_vector_value - eigen_vector[i]) <= error
        i+=1
    
    
@given( matrix_under_test = generate_data())
def test_deflate(matrix_under_test):
    try:
        _deflated_matrix , eigen_value , eigen_vector , error = deflate(matrix_under_test)
    except:
        pass

    numpy_eigen_values , numpy_eigen_vectors = linear.eig(matrix_under_test)
    # print(abs(numpy_eigen_values[0]-eigen_value),error)
    note("deflated eigen value diff %r"% abs(numpy_eigen_values[1]-eigen_value))
    note("error  %r"% error)

    assert abs(numpy_eigen_values[1]- eigen_value) <= error
    
    i= 0
    for eigen_vector_value in numpy_eigen_vectors[1]:
        
        note(" eigen vector value diff %r"%  abs(eigen_vector_value-eigen_vector[i]))
        
        note("error  %r"% error)
        
        assert  abs(eigen_vector_value - eigen_vector[i]) <= error
        i+=1
if __name__ == "__main__":
    test_power_method()
    # test_deflate()