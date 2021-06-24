from DoMain import Function
import math
import sys

ceil = Function(math.ceil)
comb = Function(math.comb)
copysign = Function(math.copysign)
fabs = Function(math.fabs)
factorial = Function(math.factorial)
floor = Function(math.floor)
fmod = Function(math.fmod)
frexp = Function(math.frexp)
fsum = Function(math.fsum)
isinf = Function(math.isinf)
isnan = Function(math.isnan)
ldexp = Function(math.ldexp)
modf = Function(math.modf)
trunc = Function(math.trunc)
exp = Function(math.exp)
log = Function(math.log)
log1p = Function(math.log1p)
log10 = Function(math.log10)
math_pow = Function(math.pow)
sqrt = Function(math.sqrt)
acos = Function(math.acos)
asin = Function(math.asin)
atan = Function(math.atan)
atan2 = Function(math.atan2)
cos = Function(math.cos)
hypot = Function(math.hypot)
sin = Function(math.sin)
tan = Function(math.tan)
degrees = Function(math.degrees)
radians = Function(math.radians)
acosh = Function(math.acosh)
asinh = Function(math.asinh)
atanh = Function(math.atanh)
cosh = Function(math.cosh)
sinh = Function(math.sinh)
tanh = Function(math.tanh)
if sys.version_info.minor >= 2:
    isfinite = Function(math.isfinite)
    expm1 = Function(math.expm1)
    erf = Function(math.erf)
    erfc = Function(math.erfc)
    gamma = Function(math.gamma)
    lgamma = Function(math.lgamma)
if sys.version_info.minor >= 3:
    log2 = Function(math.log2)
if sys.version_info.minor >= 5:
    gcd = Function(math.gcd)
    isclose = Function(math.isclose)
if sys.version_info.minor >= 7:
    remainder = Function(math.remainder)
if sys.version_info.minor >= 8:
    isqrt = Function(math.isqrt)
    perm = Function(math.perm)
    prod = Function(math.prod)
    dist = Function(math.dist)
if sys.version_info.minor >= 9:
    lcm = Function(math.lcm)
    nextafter = Function(math.nextafter)
    ulp = Function(math.ulp)

del Function
del math
del sys