import pandas as pd
from elixirfp.optimization import optimize_fingerprint

def test_optimize_fingerprint():
    df = pd.DataFrame({
        'SMILES': ['CCO', 'CCC', 'CCN', 'CNC', 'NNC'],  # Increased to 5 samples
        'Value': [1.2, 0.5, 1.8, 2.1, 0.9]
    })
    # Reduce the number of splits to match the number of samples
    best_n_bits, best_params, best_score, best_importances = optimize_fingerprint(df, "Morgan", (8, 1024))  # Using 3 splits
    assert best_n_bits >= 8 and best_n_bits <= 1024
    assert best_params is not None
    assert best_score < 0
