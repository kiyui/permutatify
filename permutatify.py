#!/bin/env python3

import argparse
from permutate import permutate

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='generate a list of permutated values')
    parser.add_argument('gen_string', metavar='gen_string', help='input [["a", "b"], ["c", "d"]] will generate ac, ad, bc, bd')
    args = parser.parse_args()

    try:
        permutation = eval(args.gen_string)
        permutations = permutate(permutation, [''])
        for mutation in permutations:
            print(mutation)
    except:
        print('invalid permutation generator string')
