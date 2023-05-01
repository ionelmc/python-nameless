__version__ = '1.0.0'
try:
    from ._nameless import longest
except ImportError:

    def longest(args):
        return max(args, key=len)
