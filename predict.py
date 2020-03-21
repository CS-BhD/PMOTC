from file_process import *
from feature_extract import *
from model import *
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Using Optimal tripeptide composition to predict unknown proteins.")
    parser.add_argument('--file', required=True, help="input fasta file")
    parser.add_argument('--out', help='output file')
    args = parser.parse_args()
    fasta = read_file.read_fasta(args.file)
    protein, encoding = TPC.tpc(fasta)
    clf = load_model.load_model()
    Optima_TPC = load_model.feature_select(encoding)
    result = clf.predict(Optima_TPC)
    write_file.write_result(args.out, protein, result)
