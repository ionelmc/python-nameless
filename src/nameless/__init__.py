from .core import compute

try:
    from ._version import version as __version__
except ImportError:
    __version__ = "0.1.0"

__all__ = [
    "compute",
]
