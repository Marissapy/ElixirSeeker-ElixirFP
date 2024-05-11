import pytest
from elixirfp.fingerprints import generate_fingerprints

def test_generate_morgan_fingerprints():
    smiles = "CCO"  # Ethanol
    result = generate_fingerprints(smiles, "Morgan", 2048)
    assert len(result) == 2048  # Ensures the fingerprint is of the correct length
    assert sum(result) > 0  # Simple check to ensure some bits are set

def test_generate_topological_fingerprints():
    smiles = "CCC"  # Propane
    result = generate_fingerprints(smiles, "Topological", 1024)
    assert len(result) == 1024
    assert sum(result) > 0

def test_generate_maccs_fingerprints():
    smiles = "CCN"  # Ethylamine
    result = generate_fingerprints(smiles, "MACCS", 166)  # MACCS keys
    assert len(result) == 167  # Correct length including the zeroth position

