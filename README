# permutatify
A Python script and module for generating permutations of a string

## script
Script usage:
```
usage: permutatify.py [-h] gen_string

generate a list of permutated values

positional arguments:
  gen_string  input [["a", "b"], ["c", "d"]] will generate ac, ad, bc, bd

optional arguments:
  -h, --help  show this help message and exit
```
Example input:
```
./permutatify.py "[['correct', 'wrong'], ['battery'], ['', ' '], ['staple', 'pencil']]"
```
Example output:
```
correctbatterystaple
correctbatterypencil
correctbattery staple
correctbattery pencil
wrongbatterystaple
wrongbatterypencil
wrongbattery staple
wrongbattery pencil
```

## module
Simply copy over the `permutate` module folder and import it:
```python
from permutate import permutate
```
The API is as so:
```python
permutate(list_of_lists, initial_reduce_value)
permutate([['correct', 'wrong'], ['battery'], ['', ' '], ['staple', 'pencil']], [''])
```
See `test.py` for more examples.

## license
See `LICENSE`
