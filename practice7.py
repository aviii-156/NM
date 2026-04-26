#implementation of gauss jordan method
import numpy as np
A=np.array([[2,1,-1],[3,3,9],[1,2,4]],dtype=float)
b=np.array([8,0,5],dtype=float)
#convert to sympy matrix
import sympy as sp
aug=sp.Matrix(np.hstack((A,b.reshape(-1,1)))) #here -1 calculate the daimention of b and 1 is coloumn 
#reduce to row echelon form
rref_matrix,_=aug.rref()
print("Row Echelon Form:\n",rref_matrix)
#extract solution
solution =[rref_matrix[i,-1] for i in range(rref_matrix.rows)]
print("The solution is:",solution)