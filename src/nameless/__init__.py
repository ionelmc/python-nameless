__version__ = '0.1.0'

from ._nameless import ffi as _ffi
from ._nameless import lib as _lib


def longest(args):
    args = [_ffi.new('char[]', arg) for arg in args]
    result = _lib.longest(len(args), _ffi.new('char *[]', args))
    if result == _ffi.NULL:
        return ''
    else:
        return _ffi.string(result)
