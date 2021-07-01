cdef class Function:
    def __init__(Function self, object f):
        if callable(f):
            self.f = f
        elif type(f) in [staticmethod,classmethod]:
            self.f = f
        else:
            raise TypeError("Do.Function constructor argument must be callable")
    def __call__(Function self, *args, **kwargs):
        cdef Call c = Call(self.f,<tuple>args,<dict>kwargs)
        return Struct(c)

cdef class Struct:
    def __init__(Struct self, Call value):
        self._INTERNAL_VALUE_ = value
    def __hash__(Struct self):
        return id(self)
    def __getattr__(self, object key):
        # key is not in self
        return bin_op(op_extract,self,key)
    def __setattr__(Struct self, object key, object value):
        if isinstance(value,Struct):
            self._INTERNAL_VALUE_ = Call(op_place,(self._INTERNAL_VALUE_,key,(<Struct>value)._INTERNAL_VALUE_),{})
        else:
            self._INTERNAL_VALUE_ = Call(op_place,(self._INTERNAL_VALUE_,key,value),{})
    def __pos__(Struct a):
        return uni_op(op_pos,a)
    def __neg__(Struct a):
        return uni_op(op_neg,a)
    def __invert__(Struct a):
        return uni_op(op_invert,a)
    def __abs__(object a):
        return uni_op(abs,a)
    def __add__(object a, object b):
        return bin_op(op_add,a,b)
    def __sub__(object a, object b):
        return bin_op(op_sub,a,b)
    def __mul__(object a, object b):
        return bin_op(op_mul,a,b)
    def __truediv__(object a, object b):
        return bin_op(op_truediv,a,b)
    def __floordiv__(object a, object b):
        return bin_op(op_floordiv,a,b)
    def __mod__(object a, object b):
        return bin_op(op_mod,a,b)
    def __pow__(object a, object b, object c):
        return ter_op(op_pow,a,b,c)
    def __eq__(object a, object b):
        return bin_op(op_eq,a,b)
    def __ne__(object a, object b):
        return bin_op(op_ne,a,b)
    def __lt__(object a, object b):
        return bin_op(op_lt,a,b)
    def __gt__(object a, object b):
        return bin_op(op_gt,a,b)
    def __le__(object a, object b):
        return bin_op(op_le,a,b)
    def __ge__(object a, object b):
        return bin_op(op_ge,a,b)

cdef Struct uni_op(object func, Struct x):
    # func is a callable with 1 positional argument
    cdef Call c = Call(func,(x._INTERNAL_VALUE_,),{})
    return Struct(c)

cdef Struct bin_op(object func, object a, object b):
    # func is a callable with 2 positional arguments
    if isinstance(a,Struct):
        a = (<Struct>a)._INTERNAL_VALUE_
    if isinstance(b,Struct):
        b = (<Struct>b)._INTERNAL_VALUE_
    cdef Call c = Call(func,(a,b),{})
    return Struct(c)

cdef Struct ter_op(object func, object a, object b, object x):
    # func is callable with 3 positional arguments
    if isinstance(a,Struct):
        a = (<Struct>a)._INTERNAL_VALUE_
    if isinstance(b,Struct):
        b = (<Struct>b)._INTERNAL_VALUE_
    if isinstance(x,Struct):
        x = (<Struct>x)._INTERNAL_VALUE_
    cdef Call c = Call(func,(a,b,x),{})
    return Struct(c)

def op_extract(obj,key):
    return getattr(obj,key)

def op_place(obj,key,value):
    setattr(obj,key,value)
    return obj

def op_pos(a):
    return +a

def op_neg(a):
    return -a

def op_invert(a):
    return ~a

def op_add(a,b):
    return a + b

def op_sub(a,b):
    return a - b

def op_mul(a,b):
    return a * b

def op_truediv(a,b):
    return a / b

def op_floordiv(a,b):
    return a // b

def op_mod(a,b):
    return a % b

def op_pow(a,b,m):
    return pow(a,b,m)

def op_eq(a,b):
    return a == b

def op_ne(a,b):
    return a != b

def op_lt(a,b):
    return a < b

def op_gt(a,b):
    return a > b

def op_le(a,b):
    return a <= b

def op_ge(a,b):
    return a >= b

cdef class Call:
    def __init__(Call self, object func, tuple args, dict kwargs):
        self.func = func
        self.args = list(args)
        self.kwargs = kwargs
        self.klist = list(kwargs)
        self.parent = None
        self.spot = 0
        if len(self.args) != 0:
            self.mode = 0
        elif len(self.klist) != 0:
            self.mode = 1
        else:
            self.mode = 2
        # unwrap any Structs hiding in the arguments
        cdef long i
        cdef object k
        cdef str key
        for i in range(len(self.args)):
            k = self.args[i]
            if isinstance(k,Struct):
                self.args[i] = (<Struct>k)._INTERNAL_VALUE_
        for key in self.klist:
            k = self.kwargs[key]
            if isinstance(k,Struct):
                self.kwargs[key] = (<Struct>k)._INTERNAL_VALUE_
    cdef void advance(Call self):
        # we will only ever call this if
        # we know that self.mode is 0 or 1
        self.spot += 1
        if self.mode == 0:
            if self.spot >= len(self.args):
                if len(self.klist) > 0:
                    self.mode = 1
                    self.spot = 0
                else:
                    self.mode = 2
        else:
            # self.mode =1 
            if self.spot >= len(self.klist):
                self.mode = 2
    cdef object get(Call self):
        # we will only ever call this if
        # we know that self.mode is 0 or 1
        if self.mode == 0:
            return self.args[self.spot]
        else:
            return self.kwargs[self.klist[self.spot]]
    cdef void put(Call self, object value):
        # we will only ever call this if
        # we know that self.mode is 0 or 1
        if self.mode == 0:
            self.args[self.spot] = value
        else:
            self.kwargs[self.klist[self.spot]] = value

def run(Struct root):
    cdef Call elem = root._INTERNAL_VALUE_
    cdef object value
    cdef Call new_call
    while True:
        if elem.mode == 2:
            # ready to run
            value = elem.func(*elem.args,**elem.kwargs)
            if isinstance(value,Struct):
                # the result of the function call is another function call
                # replace the current function call with the new function call
                new_call = (<Struct>value)._INTERNAL_VALUE_
                new_call.parent = elem.parent
                elem = new_call
                new_call = None
            else:
                # the result is an actual value
                # not a function call
                # place the result in the appropriate location
                if elem.parent is None:
                    # this is the original function call
                    # the result is the result of the entire algorithm
                    return value
                else:
                    # move to the parent
                    # set the appropriate value in the parent
                    # to the computed value
                    # advance the parent's counter
                    elem = elem.parent
                    elem.put(value)
                    elem.advance()
        else:
            # need to cycle through arguments
            value = elem.get()
            if isinstance(value,Call):
                # we can't know the value of this argument yet
                # run it before moving to the next argument
                (<Call>value).parent = elem
                elem = <Call>value
            else:
                # this argument is just an orginary value
                # pass over it
                elem.advance()