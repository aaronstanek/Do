from DoMain import Function
import sys

abs = Function(abs)
all = Function(all)
any = Function(any)
ascii = Function(ascii)
bin = Function(bin)
bool = Function(bool)
bytearray = Function(bytearray)
bytes = Function(bytes)
chr = Function(chr)
classmethod = Function(classmethod)
compile = Function(compile)
complex = Function(complex)
delattr = Function(delattr)
dict = Function(dict)
dir = Function(dir)
divmod = Function(divmod)
enumerate = Function(enumerate)
eval = Function(eval)
exec = Function(exec)
filter = Function(filter)
float = Function(float)
format = Function(format)
frozenset = Function(frozenset)
getattr = Function(getattr)
globals = Function(globals)
hasattr = Function(hasattr)
hash = Function(hash)
help = Function(help)
hex = Function(hex)
id = Function(id)
input = Function(input)
int = Function(int)
isinstance = Function(isinstance)
issubclass = Function(issubclass)
iter = Function(iter)
len = Function(len)
list = Function(list)
locals = Function(locals)
map = Function(map)
max = Function(max)
memoryview = Function(memoryview)
min = Function(min)
next = Function(next)
object = Function(object)
oct = Function(oct)
open = Function(open)
ord = Function(ord)
pow = Function(pow)
print = Function(print)
property = Function(property)
range = Function(range)
repr = Function(repr)
reversed = Function(reversed)
round = Function(round)
set = Function(set)
setattr = Function(setattr)
slice = Function(slice)
sorted = Function(sorted)
staticmethod = Function(staticmethod)
str = Function(str)
sum = Function(sum)
super = Function(super)
tuple = Function(tuple)
type = Function(type)
vars = Function(vars)
zip = Function(zip)
if sys.version_info.minor >= 2:
    callable = Function(callable)
if sys.version_info.minor >= 7:
    breakpoint = Function(breakpoint)

del Function