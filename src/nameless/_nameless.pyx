# cython: linetrace=True, language_level=3str

def main(args):
    return max(args, key=len)
