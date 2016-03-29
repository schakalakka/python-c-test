from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = 'Hi world app',
    ext_modules = cythonize("cyfib_static.pyx"),
)