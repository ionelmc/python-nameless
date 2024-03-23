try:
    from ._core import compute
except ImportError:

    def compute(args):
        return max(args, key=len)
