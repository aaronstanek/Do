import sys
if sys.version_info.major != 3:
    raise Exception("Only Python 3 is supported by this package.")
del sys

from .DoMain import Function, Struct, run
from .DoWrap import wrap, DuplicateKeyError
from .DoBuiltIn import *
from .DoMath import *
from .DoComplex import *

del DoMain
del DoWrap
del DoBuiltIn
del DoMath
del DoComplex