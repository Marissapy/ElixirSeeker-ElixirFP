from rdkit import Chem
from rdkit.Chem import AllChem, MACCSkeys
import numpy as np

def generate_fingerprints(smiles, fp_type="Morgan", n_bits=2048):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return np.zeros(n_bits)
    if fp_type == "Morgan":
        return np.array(AllChem.GetMorganFingerprintAsBitVect(mol, radius=2, nBits=n_bits), dtype=int)
    elif fp_type == "Topological":
        return np.array(Chem.RDKFingerprint(mol, fpSize=n_bits), dtype=int)
    elif fp_type == "MACCS":
        return np.array(MACCSkeys.GenMACCSKeys(mol), dtype=int)
    return np.zeros(n_bits)
