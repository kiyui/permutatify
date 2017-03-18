#!/bin/env python3

import argparse

shift = lambda list: (list[:1], list[1:])
combine = lambda a, b: list(map(lambda i: list(map(lambda ii: i + ii, b)), a))
flatten = lambda list: [ii for i in list for ii in i]

def permutate (list, current):
    if (len(list) == 0):
        return current
    else:
        front, remainder = shift(list)
        next = flatten(combine(current, flatten(front)))
        return permutate(remainder, next)

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
