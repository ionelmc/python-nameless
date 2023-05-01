__version__ = '0.1.0'
try:
    from ._nameless import longest
except ImportError:

    def longest(args):
        return max(args, key=len)
