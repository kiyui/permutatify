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
