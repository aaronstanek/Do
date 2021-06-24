from DoMain cimport Function

@Function
def build_identity(object x):
    return x

@Function
def build_tuple(*args):
    return args

@Function
def build_list(*args):
    return list(args)

@Function
def build_set(*args):
    return set(args)

class DuplicateKeyError(Exception):
    pass

@Function
def build_dict(*args):
    cdef dict output = {}
    cdef unsigned long long i
    cdef object key
    for i in range(0,len(args),2):
        key = args[i]
        if key in output:
            raise DuplicateKeyError()
        else:
            output[key] = args[i+1]
    return output

@Function
def wrap_recur_tuple(dict switch, tuple x):
    cdef list args = []
    cdef object item
    cdef object func
    for item in x:
        func = switch.get(type(item))
        if func is None:
            args.append(item)
        else:
            args.append(func(switch,item))
    return build_tuple(*args)

@Function
def wrap_recur_list(dict switch, list x):
    cdef list args = []
    cdef object item
    cdef object func
    for item in x:
        func = switch.get(type(item))
        if func is None:
            args.append(item)
        else:
            args.append(func(switch,item))
    return build_list(*args)

@Function
def wrap_recur_set(dict switch, set x):
    cdef list args = []
    cdef object item
    cdef object func
    for item in x:
        func = switch.get(type(item))
        if func is None:
            args.append(item)
        else:
            args.append(func(switch,item))
    return build_set(*args)

@Function
def wrap_recur_dict(dict switch, dict x):
    cdef list args = []
    cdef object key
    cdef object value
    cdef object func
    for key in x:
        func = switch.get(type(key))
        if func is None:
            args.append(key)
        else:
            args.append(func(switch,key))
        value = x[key]
        func = switch.get(type(value))
        if func is None:
            args.append(value)
        else:
            args.append(func(switch,value))
    return build_dict(*args)

cdef class wrapClass(object):
    cdef dict switch
    cdef set original_types
    def __init__(wrapClass self):
        self.switch = {
            tuple: wrap_recur_tuple,
            list: wrap_recur_list,
            set: wrap_recur_set,
            dict: wrap_recur_dict
        }
        self.original_types = {
            tuple, list, set, dict
        }
    def __call__(wrapClass self, object x):
        cdef object func = self.switch.get(type(x))
        if func is None:
            return build_identity(x)
        else:
            return func(self.switch,x)
    def add(wrapClass self, object key, object func):
        if type(key) != type:
            raise TypeError("wrap.add first argument must be a type")
        if key in self.original_types:
            raise ValueError("wrap.add first argument may not be tuple, list, set, or dict")
        if type(func) != Function:
            raise TypeError("wrap.add second argument must be a Do.Function object")
        self.switch[key] = func
    def remove(wrapClass self, object key):
        if type(key) != type:
            raise TypeError("wrap.remove first argument must be a type")
        if key in self.original_types:
            raise ValueError("wrap.remove first argument may not be tuple, list, set, or dict")
        if key in self.switch:
            del self.switch[key]
    def query(wrapClass self, object key):
        if type(key) != type:
            raise TypeError("wrap.query first argument must be a type")
        return self.switch.get(key)

wrap = wrapClass()