import pytest
from elixirfp.optimization import optimize_fingerprint
import pandas as pd

def test_optimize_fingerprint():
    df = pd.DataFrame({
        'SMILES': ['CCO', 'CCC', 'CCN'],
        'Value': [1.2, 0.5, 1.8]
    })
    best_n_bits, best_params, best_score, best_importances = optimize_fingerprint(df, "Morgan", (8, 1024))
    assert best_n_bits >= 8 and best_n_bits <= 1024
    assert best_params is not None
    assert best_score < 0  # assuming scoring method that returns negative values
