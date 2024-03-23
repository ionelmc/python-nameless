# cython: linetrace=True, language_level=3str

def compute(args):
    return max(args, key=len)
