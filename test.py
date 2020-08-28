"""
file used for tests
"""
from poly import Polynomial, Monomial

def polyPrint():
    monos = [
        Monomial(3, {'a': 1, 'b': 2}),
        Monomial(2, {'b': 2}),
        Monomial(1, {'c': 3, 'a': 1}),
        Monomial(-3, {'b': 2})
    ]
    poly = Polynomial()
    for mono in monos:
        poly.addMonomial(mono)
    print(poly.toString())

def monoOps():
    mono0 = Monomial(0)
    mono1 = Monomial(4)
    mono2 = Monomial(3,  {'x': 3, 'y': 2})
    mono3 = Monomial(2, {'z': 4, 'y': 1})
    mono4 = Monomial(3,  {'x': 3, 'y': 2})

    mono1m2 = mono1.multiply(mono2)
    mono3m4 = mono3.multiply(mono4)
    mono4m3 = mono4.multiply(mono3)
    mono0m3 = mono0.multiply(mono3)
    mono3m0 = mono3.multiply(mono0)

    print(mono1m2.toString())
    print(mono3m4.toString())
    print(mono4m3.toString())
    print(mono0m3.toString())
    print(mono3m0.toString())

def polyMonoOps():
    mono0 = Monomial(0)
    mono1 = Monomial(4)
    mono2 = Monomial(-3,  {'x': 4, 'y': 2})

    poly0 = Polynomial()
    mono3 = Monomial(-2, {'z': 4, 'y': 1})
    mono4 = Monomial(3,  {'x': 3, 'y': 2})
    poly1 = Polynomial()
    poly1.addMonomials([mono3, mono4])
    poly2 = Polynomial()
    poly2.addMonomials([mono0, mono1, mono2])
    
    poly0m1 = poly0.multiplyMonomial(mono1)
    poly0m4 = poly0.multiplyMonomial(mono4)
    poly2m4 = poly2.multiplyMonomial(mono4)
    poly1m2 = poly1.multiplyMonomial(mono2)

    print(poly0m1.toString())
    print(poly0m4.toString())
    print(poly2m4.toString())
    print(poly1m2.toString())

def polyOps():
    mono0 = Monomial(0)
    mono1 = Monomial(4)
    mono2 = Monomial(-3,  {'x': 4, 'y': 2})
    mono3 = Monomial(-2, {'z': 4, 'y': 1})
    mono4 = Monomial(3,  {'x': 3, 'y': 2})
    mono5 = Monomial(-7,  {'t': 5, 'z': 6, 'm': 7})
    mono6 = Monomial(1, {'x': 2, 'y': 2})

    poly0 = Polynomial()
    poly1 = Polynomial()
    poly1.addMonomials([mono3])
    poly2 = Polynomial()
    poly2.addMonomials([mono0, mono1, mono2])
    poly3 = Polynomial()
    poly3.addMonomials([mono1, mono3])
    poly4 = Polynomial()
    poly4.addMonomials([mono5, mono3, mono2, mono4])
    poly5 = Polynomial()
    poly5.addMonomials([mono2, mono4])
    poly6 = Polynomial()
    poly6.addMonomials([mono6, mono4])

    p0m4 = poly0.multiply(poly4)
    p4m0 = poly4.multiply(poly0)
    p2m3 = poly2.multiply(poly3)
    p3m2 = poly3.multiply(poly2)
    p2m4 = poly2.multiply(poly4)
    p5m6 = poly5.multiply(poly6)

    print(p0m4.toString())
    print(p4m0.toString())
    print(p2m3.toString())
    print(p3m2.toString())
    print(p2m4.toString())
    print(p5m6.toString())

def polyPow():
    mono1 = Monomial(1, {'a': 1})
    mono2 = Monomial(1, {'b': 1})
    mono3 = Monomial(-2, {'x': 1, 'y': 1})
    mono4 = Monomial(1, {'c': 1})

    #poly0 = Polynomial()
    poly1 = Polynomial()
    poly1.addMonomials([mono1, mono2]) 
    poly2 = Polynomial()
    poly2.addMonomials([mono1, mono2, mono4])
    poly3 = Polynomial()
    poly3.addMonomials([mono3, mono2, mono1])
    poly4 = Polynomial()
    poly4.addMonomials([mono3])
   


    #p0p0 = poly0.power(0)
    p1p0 = poly1.power(0)
    p2p2 = poly2.power(2)
    p1p2 = poly1.power(2)
    p1p4 = poly1.power(4)
    p3p2 = poly3.power(2)
    p4p5 = poly4.power(5)


    #print(p0p0.toString())
    print(p1p0.toString())
    print(p2p2.toString())
    print(p1p2.toString())
    print(p1p4.toString())
    print(p3p2.toString())
    print(p4p5.toString())
    





if __name__ == '__main__':
    #polyPrint()
    #monoOps()
    #polyMonoOps()
    #polyOps()
    polyPow()