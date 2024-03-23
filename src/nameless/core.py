from ._core import ffi as _ffi
from ._core import lib as _lib


def main(args):
    args = [_ffi.new("char[]", arg.encode()) for arg in args]
    result = _lib.main(len(args), _ffi.new("char *[]", args))
    if result == _ffi.NULL:
        return None
    else:
        return _ffi.string(result).decode()
