# ElixirFP
ElixirFP is a robust Python library designed for the generation and optimization of molecular fingerprints, crucial tools in computational chemistry for drug discovery and chemical informatics. In the realm of computational drug discovery, the ElixirFP package is potentially emerged as an essential tool, enhancing the functionality and interpretability of molecular fingerprint analysis. Developed as part of our ongoing research efforts, ElixirFP is equipped to generate three prevalent types of molecular fingerprints: Morgan, Topological, and MACCS. Each type provides a unique perspective on chemical properties and interactions, offering flexibility for researchers to select the most appropriate fingerprint for their specific needs. Moreover, ElixirFP excels in determining the optimal fingerprint length, utilizing advanced algorithms to balance information retention and computational efficiency, thereby enhancing the performance of subsequent analyses. A critical functionality of ElixirFP is its capability to deliver importance scores for individual fingerprint bits, particularly MACCS fingerprints. These scores are invaluable for understanding which molecular components significantly impact biological activity, thus improving the interpretability of results and enabling researchers to identify key chemical structures predictive of activity.


![image](https://github.com/Marissapy/ElixirSeeker-ElixirFP/assets/119525086/06f6c1c7-ae67-46df-9b15-819098cc5669)

The integration of Kernel PCA (KPCA) with Gaussian Radial Basis Function (RBF) kernel within ElixirFP further distinguishes this package by generating weighted fingerprints based on derived importance scores. This approach captures complex and nonlinear relationships within the data, significantly enhancing both the accuracy and interpretability of the fingerprints. The benefits of using ElixirFP in drug discovery are manifold. Firstly, the package enhances predictive accuracy by optimizing fingerprint lengths and employing weighted KPCA, proving crucial for the effective identification of potential therapeutic compounds. Secondly, it increases interpretability, particularly through the importance scores provided for MACCS fingerprints, which offer clear insights into influential molecular features. Lastly, ElixirFP's efficient data processing capabilities not only reduce computational demands but also accelerate the drug discovery process, thereby supporting researchers in their quest to uncover new therapeutics. Overall, ElixirFP represents a comprehensive solution that facilitates advanced data processing techniques and provides detailed insights into molecular structures, significantly boosting the discovery and development of effective anti-aging treatments.




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
