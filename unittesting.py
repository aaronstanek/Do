import unittest
import Do

@Do.Function
def fib(n):
    if n < 3:
        return 1
    else:
        output = fib(n-2)
        output += fib(n-1)
        return output

@Do.Function
def ack(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ack(m-1,1)
    else:
        return ack(m-1,ack(m,n-1))

@Do.Function
def fact(n):
    if n < 2:
        return 1
    else:
        return n * fact(n-1)

class example(object):
    pass

@Do.Function
def make_example():
    return example()

@Do.Function
def inner_example():
    output = make_example()
    output.red = 3
    output.green = False
    output.blue = "hello"
    return output

@Do.Function
def outer_example():
    data = inner_example()
    output = data.blue * data.red
    output += data.green * "world"
    return output

@Do.Function
def returns_60():
    return 60

@Do.Function
def returns_10():
    return 10

@Do.Function
def returns_5():
    return 5

@Do.Function
def returns_1():
    return 1

@Do.Function
def returns_True():
    return True

@Do.Function
def returns_False():
    return False

@Do.Function
def pos_test():
    return +returns_60()

@Do.Function
def neg_test():
    return -returns_60()

@Do.Function
def invert_test():
    return ~returns_60()

@Do.Function
def sub_test():
    a = returns_60()
    b = returns_10()
    return a - b

@Do.Function
def truediv_test():
    a = returns_60()
    b = returns_10()
    return a / b

@Do.Function
def floordiv_test():
    a = returns_60() + 11
    b = returns_10()
    return a // b

@Do.Function
def mod_test():
    a = returns_60() - 7
    b = returns_10()
    return a % b

@Do.Function
def pow_test1():
    a = returns_10()
    b = returns_60() // 10
    return a ** b

@Do.Function
def pow_test2():
    a = returns_10() + 7
    b = returns_10()
    c = returns_60()
    return pow(a,b,c)

@Do.Function
def compare_test():
    output = []

    output.append( returns_10() == returns_60() ) # False
    output.append( returns_60() == returns_10() ) # False
    output.append( returns_60() == 60 ) # True

    output.append( returns_10() != returns_60() ) # True
    output.append( returns_60() != returns_10() ) # True
    output.append( returns_60() != 60 ) # False

    output.append( returns_10() < returns_60() ) # True
    output.append( returns_60() < returns_10() ) # False
    output.append( returns_60() < returns_60() ) # False

    output.append( returns_10() > returns_60() ) # False
    output.append( returns_60() > returns_10() ) # True
    output.append( returns_60() > returns_60() ) # False

    output.append( returns_10() <= returns_60() ) # True
    output.append( returns_60() <= returns_10() ) # False
    output.append( returns_60() <= returns_60() ) # True

    output.append( returns_10() >= returns_60() ) # False
    output.append( returns_60() >= returns_10() ) # True
    output.append( returns_60() >= returns_60() ) # True

    return Do.wrap(output)

@Do.Function
def sqrt_test(n):
    if n <= 0:
        return Do.sqrt(65536)
    else:
        return Do.sqrt(sqrt_test(n-1))

class StateTester(object):
    def __init__(self):
        self.value = 0
    def increment_by(self,value):
        self.value += value

class TestStringMethods(unittest.TestCase):

    def test_fib(self):
        # basic functioning
        # addition
        self.assertEqual( Do.run(fib(6)) , 8 )

    def test_ack(self):
        # multiple arguments
        # call within a call
        self.assertEqual( Do.run(ack(2,2)) , 7 )
    
    def test_fact(self):
        # multiplication
        self.assertEqual( Do.run(fact(10)) , 3628800 )

    def test_get_set(self):
        # test dot operations
        # test non-tree graph
        self.assertEqual( Do.run(outer_example()) , "hellohellohello" )

    def test_pos(self):
        # pos
        self.assertEqual( Do.run(pos_test()) , 60 )

    def test_neg(self):
        # neg
        self.assertEqual( Do.run(neg_test()) , -60 )
    
    def test_invert(self):
        # invert
        self.assertEqual( Do.run(invert_test()) , -61 )
    
    def test_abs(self):
        # abs
        # neg
        self.assertEqual( Do.run(abs(neg_test())) , 60 )

    def test_sub(self):
        # subtraction
        self.assertEqual( Do.run(sub_test()) , 50 )
    
    def test_truediv(self):
        # true division
        self.assertEqual( Do.run(truediv_test()) , 6.0 )
    
    def test_floordiv(self):
        # floor division
        self.assertEqual( Do.run(floordiv_test()) , 7 )
    
    def test_mod(self):
        # mod
        self.assertEqual( Do.run(mod_test()) , 3 )
    
    def test_pow(self):
        # pow
        # floor division
        # addition
        self.assertEqual( Do.run(pow_test1()) , 1000000 )
        self.assertEqual( Do.run(pow_test2()) , pow(17,10,60) )

    def test_shifts(self):
        # lshift
        # rshift
        self.assertEqual( Do.run( returns_5() << returns_1() ) , 5 << 1 )
        self.assertEqual( Do.run( returns_5() >> returns_1() ) , 5 >> 1 )

    def test_boolean_operations(self):
        # and
        # or
        # xor
        values = [(True,returns_True),(False,returns_False)]
        for a in values:
            for b in values:
                self.assertEqual( Do.run( a[1]() & b[1]() ) , a[0] & b[0] )
                self.assertEqual( Do.run( a[1]() | b[1]() ) , a[0] | b[0] )
                self.assertEqual( Do.run( a[1]() ^ b[1]() ) , a[0] ^ b[0] )

    def test_wrapping_type(self):
        self.assertTrue(isinstance(Do.wrap( () ),Do.Struct))
        self.assertTrue(isinstance(Do.wrap( (1,2,3) ),Do.Struct))
        self.assertTrue(isinstance(Do.wrap( [] ),Do.Struct))
        self.assertTrue(isinstance(Do.wrap( [1,2,3] ),Do.Struct))
        self.assertTrue(isinstance(Do.wrap( set() ),Do.Struct))
        self.assertTrue(isinstance(Do.wrap( {1,2,3} ),Do.Struct))
        self.assertTrue(isinstance(Do.wrap( dict() ),Do.Struct))
        self.assertTrue(isinstance(Do.wrap( {"happy":True,"value":5} ),Do.Struct))
        self.assertTrue(isinstance(Do.wrap( 7 ),Do.Struct))
        self.assertTrue(isinstance(Do.wrap( None ),Do.Struct))
    
    def test_wrapping_value1(self):
        a = ack(2,2)
        b = [None,{"hello":a},-99]
        c = Do.wrap(b)
        self.assertEqual( Do.run(c) , [None,{"hello":7},-99] )
    
    def test_wrapping_value2(self):
        a1 = fib(6)
        a2 = fact(10)
        b = [a2,{6,False,(a1,a2)},a1]
        c = Do.wrap(b)
        self.assertEqual( Do.run(c) , [3628800,{6,False,(8,3628800)},8] )
    
    def test_wrapping_value3(self):
        f = {
            returns_10(): True,
            returns_10(): False,
            returns_60(): None
        }
        g = Do.wrap(f)
        with self.assertRaises(Do.DuplicateKeyError):
            Do.run(g)
    
    def test_wrapping_value4(self):
        f = {
            returns_10(),
            returns_10(),
            returns_60()
        }
        g = Do.wrap(f)
        self.assertEqual( Do.run(g) , {10,60} )
    
    def test_compare(self):
        y = [
            False, False, True,
            True, True, False,
            True, False, False,
            False, True, False,
            True, False, True,
            False, True, True
        ]
        self.assertEqual( Do.run(compare_test()) , y )
    
    def test_sqrt(self):
        a = Do.run(sqrt_test(2))
        self.assertTrue( abs(a-4) < 10e-6 )
    
    def test_update(self):
        a = StateTester()
        b = Do.update(a,"increment_by",8)
        c = Do.update(b,"increment_by",-4)
        self.assertEqual( Do.run(c).value , 4 )

if __name__ == '__main__':
    unittest.main()