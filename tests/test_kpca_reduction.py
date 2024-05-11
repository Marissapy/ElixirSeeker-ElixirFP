import pytest
from elixirfp.kpca_reduction import apply_kpca
import numpy as np

def test_apply_kpca():
    # Mock data for testing
    fingerprints = np.random.randint(2, size=(10, 100))  # 10 samples, 100 features
    weights = np.ones(100)
    results = apply_kpca(fingerprints, weights, n_components=5)
    assert results.shape == (10, 5)  # Check if dimension reduction was correct
