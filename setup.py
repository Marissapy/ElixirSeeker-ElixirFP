from setuptools import setup, find_packages

setup(
    name='ElixirFP',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pandas',
        'rdkit-pypi',
        'xgboost',
        'scikit-learn',
        'scipy'
    ],
    entry_points={
        'console_scripts': [
            'elixirfp=elixirfp.cli:main'
        ]
    }
)
