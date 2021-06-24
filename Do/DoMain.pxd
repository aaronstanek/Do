cdef class Function:
    cdef object f

cdef class Struct:
    cdef readonly Call _INTERNAL_VALUE_

cdef class Call:
    cdef readonly object func
    cdef readonly list args
    cdef readonly dict kwargs
    cdef list klist
    cdef public Call parent
    cdef long spot
    cdef readonly int mode
    cdef void advance(Call self)
    cdef object get(Call self)
    cdef void put(Call self, object value)