import argparse
from .optimization import optimize_fingerprint

def main():
    parser = argparse.ArgumentParser(description="Process some fingerprints.")
    parser.add_argument('smiles', type=str, help='SMILES string to process')
    args = parser.parse_args()
    
    # 假设有一个函数来处理 SMILES 字符串
    result = optimize_fingerprint(args.smiles)
    print(result)

if __name__ == '__main__':
    main()
