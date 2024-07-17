import numpy as np

A = np.array([[1, 2], [3, 4]])

# Compute A * A^T
ATA = np.dot(A, A.T)

# Compute eigenvalues and eigenvectors of A * A^T
eigenvalues, U = np.linalg.eig(ATA)

# Compute singular values from eigenvalues
singular_values = np.sqrt(np.abs(eigenvalues))

# Construct the S matrix
S = np.diag(singular_values)

# Compute V from A^T * A
ATA_T = np.dot(A.T, A)
eigenvalues_V, V = np.linalg.eig(ATA_T)

# Sort V based on eigenvalues (not necessary if A is symmetric)
sorted_indices_V = np.argsort(eigenvalues_V)[::-1]
V = V[:, sorted_indices_V]

print("U:\n", U)
print("S:\n", S)
print("V:\n", V)

svd=np.dot(U, np.dot(S, V ))
print(svd)