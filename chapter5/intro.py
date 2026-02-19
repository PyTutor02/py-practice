import dis
import itest    #importing userdefined module
def fun():
    a=10
    b=20
    print(a+b)
dis.dis(fun)