# cython: linetrace=True, language_level=3str

def longest(args):
    return max(args, key=len)
