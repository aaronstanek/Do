from DoMain import Function
import cmath
import sys

complex_phase = Function(cmath.phase)
complex_polar = Function(cmath.polar)
complex_rect = Function(cmath.rect)
complex_exp = Function(cmath.exp)
complex_log = Function(cmath.log)
complex_log10 = Function(cmath.log10)
complex_sqrt = Function(cmath.sqrt)
complex_acos = Function(cmath.acos)
complex_asin = Function(cmath.asin)
complex_atan = Function(cmath.atan)
complex_cos = Function(cmath.cos)
complex_sin = Function(cmath.sin)
complex_tan = Function(cmath.tan)
complex_acosh = Function(cmath.acosh)
complex_asinh = Function(cmath.asinh)
complex_atanh = Function(cmath.atanh)
complex_cosh = Function(cmath.cosh)
complex_sinh = Function(cmath.sinh)
complex_tanh = Function(cmath.tanh)
complex_isinf = Function(cmath.isinf)
complex_isnan = Function(cmath.isnan)
if sys.version_info.minor >= 2:
    complex_isfinite = Function(cmath.isfinite)
if sys.version_info.minor >= 5:
    complex_isclose = Function(cmath.isclose)

del Function
del cmath
del sys