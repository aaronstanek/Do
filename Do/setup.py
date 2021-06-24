# import setuptools
from distutils.core import Extension, setup
from Cython.Build import cythonize

# define an extension that will be cythonized and compiled
ext = Extension(name="DoMain", sources=["DoMain.pyx"])
setup(ext_modules=cythonize(ext,language_level=3))

# define an extension that will be cythonized and compiled
ext = Extension(name="DoWrap", sources=["DoWrap.pyx"])
setup(ext_modules=cythonize(ext,language_level=3))