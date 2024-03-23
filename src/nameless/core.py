try:
    from ._core import main
except ImportError:

    def main(args):
        return max(args, key=len)
