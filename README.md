# ElixirFP
ElixirFP is a Python library for generating and optimizing chemical fingerprints of molecules. It supports multiple types of molecular fingerprints, including Morgan, Topological, and MACCS fingerprints, and offers a method for dimensionality reduction using Kernel Principal Component Analysis (KPCA).

## Features
- Generate three types of molecular fingerprints: Morgan, Topological, and MACCS.
- Optimize the length and parameters of molecular fingerprints.
- Apply KPCA for dimensionality reduction.
## Installation
### Remote Download
You can clone the latest code repository via Git:
```bash
  git clone https://github.com/Marissapy/ElixirSeeker-ElixirFP/ElixirFP.git
  cd ElixirFP
```
To install ElixirFP and its dependencies, ensure you have Python installed in your working environment and run the following commands:
```bash
pip install -r requirements.txt
```
This will install the following required libraries:

- numpy

- pandas
- rdkit-pypi
- xgboost
- scikit-learn
- scipy
### Local Installation
After downloading the code and installing the dependencies, you can install this library with the following command:

```bash
pip install .
```
This will install ElixirFP as a package, allowing you to import it in any Python script.

## Usage
### Generating and Optimizing Fingerprints
Here is an example of how to use ElixirFP to generate and optimize chemical fingerprints in a Python environment.

```python
from elixirfp.fingerprints import generate_fingerprints
from elixirfp.optimization import optimize_fingerprint
# Generate Morgan fingerprints
smiles_string = "CCO"
morgan_fp = generate_fingerprints(smiles_string, "Morgan", 2048)
# Optimize fingerprint parameters
df = pd.DataFrame({'SMILES': ['CCO', 'CCC', 'CCN'], 'Value': [1.2, 0.5, 1.8]})
optimized_result = optimize_fingerprint(df, "Morgan", (8, 1024))
print("Optimized parameters:", optimized_result)
```
### Dimensionality Reduction with KPCA
Here is an example of how to perform dimensionality reduction using KPCA:

```python
from elixirfp.kpca_reduction import apply_kpca
# Assuming fingerprints and weights are prepared
kpca_results = apply_kpca(fingerprints, weights)
print("KPCA results:", kpca_results)
```
## License
This project is licensed under the MIT License.
