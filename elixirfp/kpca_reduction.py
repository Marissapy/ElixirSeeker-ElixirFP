from sklearn.decomposition import KernelPCA
from scipy.spatial.distance import pdist, squareform
import numpy as np

def apply_kpca(fingerprints, weights, n_components=64):
    def create_weighted_kernel_matrix(X, importances, gamma=0.01):
        weighted_distances = squareform(pdist(X, metric=lambda u, v: np.sqrt(np.sum(importances * (u - v)**2))))
        K = np.exp(-gamma * weighted_distances**2)
        return K
    
    K = create_weighted_kernel_matrix(fingerprints, weights)
    kpca = KernelPCA(n_components=n_components, kernel='precomputed')
    kpca_fingerprints = kpca.fit_transform(K)
    return kpca_fingerprints
