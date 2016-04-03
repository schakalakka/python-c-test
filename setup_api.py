from distutils.core import setup, Extension

# the c extension module
extension_mod = Extension(name="ext_fib", sources=["ext_fib.c", "fib.c"],
                          extra_link_args=[],
                          extra_compile_args=['-fPIC', '-O3', '-fno-omit-frame-pointer'],
                          )

setup(name="ext_fib", ext_modules=[extension_mod])
