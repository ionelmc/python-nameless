from pathlib import Path

from cffi import FFI

ffi = FFI()
ffi.cdef(
    """
    char* longest(int argv, char *argv[]);
    """
)


ffi.set_source(
    "nameless._nameless",
    Path(__file__).parent.joinpath("_nameless.c").read_text(),
)

if __name__ == "__main__":
    ffi.compile()
