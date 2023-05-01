__version__ = '0.1.1'
try:
    from ._nameless import longest
except ImportError:

    def longest(args):
        return max(args, key=len)
