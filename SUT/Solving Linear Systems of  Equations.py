#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np

#Calculating Permutation of A list. used to convert a matrix into a diagonally dominant one.
#by manipulating the order of the rows.
def permutation(lst): 
  
    if len(lst) == 0: 
        return [] 
  
    if len(lst) == 1: 
        return [lst] 
  
    l = [] 
    for i in range(len(lst)): 
        m = lst[i]
        remLst = lst[:i]+lst[i+1:]
        for p in permutation(remLst): 
               l.append([m] + p) 
    return l

#Checks if abs(A[i,i])> sum(Abs(A[i,j!=i])).
def CheckDiagDominant(mat):
    # Assuming a square matrix
    flag = True
    for i in range(mat.shape[0]):
        x = 2*np.abs(mat[i,i])
        y = np.sum(np.abs(mat[i,:]))
        if(x<=y):
            flag = False
            break
    return flag

#uses CheckDiagDominant and Permutation to get A diagonally dominant matrix.
def MakeItDiagDominant(mat,vec):
    m,n = mat.shape
    if(m != n):
        print("Error : Not A Square Matrix.")
        return mat
    lst = []
    for i in range(n):
        lst.append(i)
    
    per = permutation(lst)
    flag = True
    
    w = len(per)
    temp = np.empty([n,m])
    tempvec = np.zeros([n,1])
    for i in range(w):
        for j in range(n):
            temp[j] = mat[per[i][j]]
            tempvec[j] = vec[per[i][j]] 
        if(CheckDiagDominant(temp)):

            return temp,tempvec
            flag = False
            break
        if (not (flag)):
            break
    return mat,vec


# In[4]:


# solving a linear system of equations using gauss seidel.
# mat : the coeffecients matrix.
# vec : the result vector.
# init : initial solution.
#epsilon : stopping criteria.
def SolveGaussSeidel(mat,vec,init,epsilon):
    error = np.zeros([mat.shape[0],1],dtype='float64')
    print(error.shape)
    prev = np.copy(init)
    ddmat,vec = MakeItDiagDominant(mat,vec)
    print(ddmat)
    print(vec)
    #TODO : Add the Relation.
    # the Relation is R[i] = (v[i] - sigma(R[j]*A[j,j]))/A[i,i]
    # where A is the coeffecients matrix, v is the result vector and R is the solution vector
    maxError =  10000
    n = 5
    while(n>0 and maxError >epsilon) :
        for i in range(mat.shape[0]):
            x = vec[i]
            for j in range(mat.shape[1]):
                x -= (init[j]*ddmat[i,j])
            x+= init[i]*ddmat[i,i]
            x /= ddmat[i,i]
            init[i] = x
            print(x)
            error[i] = abs((init[i]-prev[i])/init[i]).astype('float64')
        n -=1
        print(error)    
        maxError = max(error)
        prev = np.copy(init)
        print(init)
        print(maxError)
    return init,maxError

# solving a linear system of equations using successive over relaxation.
# mat : the coeffecients matrix.
# vec : the result vector.
#init : initial solution.
#omega : relaxation factor.
#epsilon : stopping criteria.
def SolveSOR(mat,vec,init,omega,epsilon):
    error = np.zeros(mat.shape[0])
    prev = np.copy(init)

    ddmat,vec = MakeItDiagDominant(mat,vec)
    myvec=vec.copy()
    n = 6
    maxError = 10000
    #TODO : Add the Relation.
    # the Relation is R[i] = (v[i] - sigma(R[j]*A[j,j]))/A[i,i]
    # where A is the coeffecients matrix, v is the result vector and R is the solution vector
    while(n>0 and maxError > epsilon):
        for i in range(mat.shape[0]):
            print(vec)
            x = vec[i].copy()
            for j in range(mat.shape[1]):
                x -= (init[j]*ddmat[i,j])
            x+= init[i]*ddmat[i,i]
            x*= omega
            x /= ddmat[i,i]
            x += (1-omega)*init[i]
            print(x)
            init[i] = x
            error[i] = abs((init[i]-prev[i])/init[i]).astype(float)
        n -=1
        maxError = max(error)
        prev = np.copy(init)
    return init,maxError





# In[5]:


#TESTING.
mat = np.array([[2.0,-6.0,-1.0],[-3.0,-1.0,7.0],[-8.0,1.0,-2.0]])
vec = np.array([-38.0,-34.0,-20.0])

epsilon = 0.05
init= np.array([0.0,0.0,0.0])
result,error= SolveSOR(mat,vec,init,1.2,epsilon)
print("result :")
print(result)
print(error)


# In[ ]:




