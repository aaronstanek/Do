import time
import Do
import numpy as np

@Do.Function
def doack(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return doack(m-1,1)
    else:
        return doack(m-1,doack(m,n-1))

def pyack(m,n):
    if m == 0:
        return n + 1
    elif n == 0:
        return pyack(m-1,1)
    else:
        return pyack(m-1,pyack(m,n-1))

def main():
    do_list = []
    py_list = []
    a = time.time()
    b = time.time()
    for i in range(100):
        a = time.time()
        Do.run(doack(3,3))
        b = time.time()
        do_list.append(b-a)
        a = time.time()
        pyack(3,3)
        b = time.time()
        py_list.append(b-a)
    Do_mean = np.mean(do_list)
    Py_mean = np.mean(py_list)
    print("Do",Do_mean)
    print("Py",Py_mean)
    print("Ratio",Do_mean/Py_mean)

if __name__ == "__main__":
    main()