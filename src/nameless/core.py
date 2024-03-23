try:
    from ._nameless import main
except ImportError:

    def main(args):
        return max(args, key=len)
