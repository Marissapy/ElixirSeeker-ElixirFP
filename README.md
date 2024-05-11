# ElixirFP
ElixirFP is a robust Python library designed for the generation and optimization of molecular fingerprints, crucial tools in computational chemistry for drug discovery and chemical informatics. This library facilitates detailed analysis and representation of chemical compounds, supporting various fingerprint types including Morgan, Topological, and MACCS. Additionally, ElixirFP incorporates Kernel Principal Component Analysis (KPCA) for advanced dimensionality reduction, enhancing the ability to visualize and analyze high-dimensional chemical data.


![image](https://github.com/Marissapy/ElixirSeeker-ElixirFP/assets/119525086/06f6c1c7-ae67-46df-9b15-819098cc5669)


## Features
- Generate three types of molecular fingerprints: Morgan, Topological, and MACCS.
- Optimize the length and parameters of molecular fingerprints.
- Apply KPCA for dimensionality reduction.
- Designed with an intuitive interface, facilitating easy integration into existing workflows in drug discovery and other chemical analysis tasks.
- Improved Machine Learning Model Performance: By reducing noise and redundancy in the data, KPCA can lead to more accurate and robust predictive models in cheminformatics.
## Installation
### Remote Download
You can clone the latest code repository via Git:
```bash
  git clone https://github.com/Marissapy/ElixirSeeker-ElixirFP.git
  cd ElixirSeeker-ElixirFP/
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
