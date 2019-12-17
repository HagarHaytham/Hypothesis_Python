from hypothesis import given
import hypothesis.strategies as st
import numpy as np
import hypothesis.extra.numpy as hnp
from numpy import linalg as linear
from eigen import powerMethod, deflate


@given(matrix_under_test= hnp.arrays(dtype=np.integer, shape = hnp.array_shapes(min_dims = 2, max_dims = 2), elements=st.integers(1,10),unique = True) )
def test_power_method(matrix_under_test):
    eigen_value , eigen_vector , error = powerMethod(matrix_under_test)
    numpy_eigen_values , numpy_eigen_vectors = linear.eig(matrix_under_test)
    # print(abs(numpy_eigen_values[0]-eigen_value),error)
    assert abs(numpy_eigen_values[0] - eigen_value) <= error 
    i= 0
    for eigen_vector_value in numpy_eigen_vectors[0]:
        print(eigen_vector_value , eigen_vector[i])
        assert  abs(eigen_vector_value - eigen_vector[i]) <= error
        i+=1
    
    
@given( matrix_under_test= hnp.arrays(np.integer,shape = hnp.array_shapes(min_dims = 2, max_dims = 2), elements=st.integers(1,10),unique = True))
def test_deflate(matrix_under_test):
    deflated_matrix , eigen_value , eigen_vector , error = deflate(matrix_under_test)
    numpy_eigen_values , numpy_eigen_vectors = linear.eig(deflated_matrix)
    # print(abs(numpy_eigen_values[0]-eigen_value),error)

    assert abs(numpy_eigen_values[0]- eigen_value) <= error
    i= 0
    for eigen_vector_value in numpy_eigen_vectors[0]:
        print(eigen_vector_value , eigen_vector[i])
        assert  abs(eigen_vector_value - eigen_vector[i]) <= error
        i+=1
if __name__ == "__main__":
    test_power_method()
    test_deflate()