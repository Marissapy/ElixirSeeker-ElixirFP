import argparse
from .fingerprints import process_smiles

def main():
    parser = argparse.ArgumentParser(description="Process SMILES strings to generate fingerprints.")
    parser.add_argument('smiles', type=str, help='SMILES string to process')
    args = parser.parse_args()
    
    # 处理 SMILES 字符串
    fingerprint = process_smiles(args.smiles)
    print("Generated Fingerprint:", fingerprint)

if __name__ == '__main__':
    main()
