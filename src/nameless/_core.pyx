# cython: linetrace=True, freethreading_compatible=True

def compute(args):
    return max(args, key=len)
