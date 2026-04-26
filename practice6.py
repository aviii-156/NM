# import numpy as np
# #cofficient matrix
# A = np.array([[1,1],[2,3]],dtype=float)
# #right hand side 
# b =np.array([5,13],dtype=float)
# #gaussian elimination
# x=  np.linalg.solve(A,b) #linalg short form of linear algebra
# print("The solution is:",x)





# #2nd example
# import numpy as np
# #cofficient matrix
# A = np.array([[2,3,-1],[4,1,2],[3,-2,1]],dtype=float)
# #right hand side 
# b =np.array([5,6,4],dtype=float)
# #gaussian elimination
# x=  np.linalg.solve(A,b) #linalg short form of linear algebra
# print("The solution is:",x)



# #3rd example 
# import numpy as np
# #cofficient matrix
# A = np.array([[1,1,1,1],[2,-1,3,2],[3,2,-1,1],[4,-1,2,3]],dtype=float)
# #right hand side 
# b =np.array([10,15,10,20],dtype=float)
# #gaussian elimination
# x=  np.linalg.solve(A,b) #linalg short form of linear algebra
# print("The solution is:",x)



# find the eiganvale 
import numpy as np
#cofficient matrix
A = np.array([[4,2],[1,3]],dtype=float)
#eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)
det = np.linalg.det(A)
print("Determinant =", det)
print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)
