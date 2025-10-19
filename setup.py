#!/usr/bin/env python
import os
import re
from pathlib import Path

from setuptools import find_namespace_packages
from setuptools import setup
from setuptools.command.build_ext import build_ext
from setuptools.dist import Distribution

allow_extensions = True
# Enable this if the extensions will not build on PyPy
# if '__pypy__' in sys.builtin_module_names:
#     print('NOTICE: C extensions disabled on PyPy (would be broken)!')
#     allow_extensions = False
if os.environ.get("SETUPPY_FORCE_PURE"):
    print("NOTICE: C extensions disabled (SETUPPY_FORCE_PURE)!")
    allow_extensions = False


class OptionalBuildExt(build_ext):
    """
    Allow the building of C extensions to fail.
    """

    def run(self):
        try:
            super().run()
        except Exception as e:
            self._unavailable(e)
            self.extensions = []  # avoid copying missing files (it would fail).

    def _unavailable(self, e):
        print("*" * 80)
        print(
            """WARNING:

    An optional code optimization (C extension) could not be compiled.

    Optimizations for this package will not be available!
            """
        )

        print("CAUSE:")
        print("")
        print("    " + repr(e))
        print("*" * 80)


class BinaryDistribution(Distribution):
    """
    Distribution which almost always forces a binary package with platform name
    """

    def has_ext_modules(self):
        return super().has_ext_modules() or not os.environ.get("SETUPPY_ALLOW_PURE")


def read(*names, **kwargs):
    with Path(__file__).parent.joinpath(*names).open(encoding=kwargs.get("encoding", "utf8")) as fh:
        return fh.read()


setup(
    long_description="{}\n{}".format(
        re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub("", read("README.rst")),
        re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst")),
    ),
    long_description_content_type="text/x-rst",
    packages=find_namespace_packages("src"),
    package_dir={"": "src"},
    py_modules=[path.stem for path in Path("src").glob("*.py")],
    include_package_data=True,
    zip_safe=False,
    cmdclass={"build_ext": OptionalBuildExt},
    cffi_modules=[f"{path}:ffi" for path in Path("src").glob("**/_*_build.py")],
)
