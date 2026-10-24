import numpy as np

def pairwise_cosine_similarity(X):
    X = np.matrix(X)

    norms = np.linalg.norm(X, axis=1, keepdims=True)

    norms = np.where(norms == 0, 1, norms)

    X_norm = X / norms

    S = X_norm @ X_norm.T

    return S.tolist()