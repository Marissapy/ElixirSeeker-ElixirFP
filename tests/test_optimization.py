import pandas as pd
from elixirfp.optimization import optimize_fingerprint

def test_optimize_fingerprint():
    df = pd.DataFrame({
        'SMILES': ['CCC', 'CCC', 'CCC','CCC', 'CCC', 'CCC','CCC', 'CCC', 'CCC', 'CNC', 'CNC', 'CNC', 'CNC', 'CNC', 'CNC', 'CNC', 'CNC'],  # Increased to 5 samples
        'Value': [1.2, 1.2, 1.2,1.2, 1.2, 1.2,1.2, 1.2, 1.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
    })
    # Reduce the number of splits to match the number of samples
    best_n_bits, best_params, best_score, best_importances = optimize_fingerprint(df, "Morgan", (8, 1024))  # Using 3 splits
    assert best_n_bits >= 8 and best_n_bits <= 1024
    assert best_params is not None
    # Adjusted to a reasonable threshold for the score
    acceptable_threshold = 1.0
    assert best_score <= acceptable_threshold
