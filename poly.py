from math import comb
from mono import Monomial

class Polynomial:
    """
    fields
    ------
    terms: (dict) the key is the variables (tuple), the value is the constant(float)
    """

    def __init__(self):
        self.terms = dict()
    
    def copy(self):
        """
        return
        ------
        (Polynomial) a copy of this polynomial
        """
        poly = Polynomial()
        poly.terms = self.terms.copy()
        return poly

    def isNull(self):
        """
        return
        ------
        (bool) true if this is a null polynomial, else False
        """
        return self.terms == dict() or all(self.terms[var] == 0 for var in self.terms)


    def addMonomial(self, mono):
        """
        add mono to the polynomial

        parameters
        ----------
        mono: (Monomial)

        side effects
        ------------
        <mono> added to this polynomial
        """
        monoVar = mono.variablesToTuple()
        if not mono.isNull():
            if monoVar in self.terms:
                self.terms[monoVar] += mono.constant
            else:
                self.terms[monoVar] = mono.constant
            if self.terms[monoVar] == 0:
                self.terms.pop(monoVar)

    def addMonomials(self, monos):
        """
        add all monos's element to the polynomial

        parameters
        ----------
        monos: (list) list of monomials

        side effects
        ------------
        each monomial of <monos> added to this polynomial

        """
        for mono in monos:
            self.addMonomial(mono)

    def keyToStr(self, t):
        """
        transform tuple key in <t> to string. Used in toString()

        parameters
        ----------
        t: (tuple or list)

        return 
        ------
        (str)
        """
        res = []
        for var in t:
            if var[0] != '':
                res.append(var[0])
                res.append(str(var[1]))
        return "".join(res)

    def toString(self):
        """
        usage constraints
        -----------------
        self.terms is not empty

        return
        ------
        (str) a string representation
        """
        if not self.isNull():
            res = ""
            variables = list(self.terms.keys())
            variables.sort(key = lambda x: "".join(var[0] for var in x))
            for var in variables:
                const = self.terms[var]
                if const >= 0:
                    c = "+"+str(const)
                else:
                    c = str(const)
                res += "{} {} ".format(c, self.keyToStr(var)) 
        else:
            res = "+0"
        return res

    def getMonomials(self):
        """
        return
        ------
        (list) a list of all monomials forming the polynomial
        """
        monos = []
        for variables in self.terms:
            const = self.terms[variables]
            varbls = {v[0]: v[1] for v in variables}
            monos.append(Monomial(const, varbls))
        return monos

    def twoHalfsOfMonomials(self, monos):
        """
        parameters
        ----------
        monos: (list) list of monomials

        usage constraints
        -----------------
        the number of monomials >= 2

        return
        ------
        (list) two list. Half of the <monos>'s elements for each list.
        1st list's length >= 2nd list length
        """
        length = len(monos)
        halfLen = length // 2
        half2 = []
        for _ in range(halfLen):
            half2.append(monos.pop())
        return [monos, half2]

    def binomialExpansion(self, poly1, poly2, power):
        """
        parameters
        ----------
        poly1, poly2: (Polynomial)
        power: (int)

        return
        ------
        (Polynomial) the result of (poly1 + poly2) ** power
        """
        res = Polynomial() #a null polynomial
        for k in range(power+1):
            res = res.add(poly1.
            power(k).
            multiply(poly2.power(power-k)).
            multiplyConstant(comb(power, k)))
        return res

    def multiplyMonomial(self, mono):
        """
        parameters
        ----------
        mono: (Monomial)

        return
        ------
        (Polynomial) this polynomial multiplied by <mono>
        """
        monomials = self.getMonomials()
        poly = Polynomial()
        for m in monomials:
            poly.addMonomial(m.multiply(mono))
        return poly

    def add(self, poly):
        """
        parameters
        ----------
        poly: (Polynimial)

        return
        ------
        (Polynomial) this polynomial plus <poly>
        """
        res = self.copy()
        for variables in poly.terms:
            if variables in self.terms:
                res.terms[variables] += poly.terms[variables]
            else:
                res.terms[variables] = poly.terms[variables]
            if res.terms[variables] == 0:
                res.terms.pop(variables)
        return res

    def multiply(self, poly):
        """
        parameters
        ----------
        poly: (Polynomial)

        return
        ------
        (Polynomial) this polynomial multiplied by <poly>
        """
        res = Polynomial()
        monomials = self.getMonomials()
        for mono in monomials:
            res = res.add(poly.multiplyMonomial(mono))
        return res
    
    def multiplyConstant(self, const):
        """
        parameters
        ----------
        const: (float)

        return
        ------
        (Polynomial) this polynomial multiplied by <const>
        if const is null, a null Polynomial is returned
        """

        if const != 0:
            res = self.copy()
            for variables in res.terms:
                res.terms[variables] *= const
        else:
            res = Polynomial()
        return res
                
    def power(self, p):
        """
        powers the polynomial to p

        parameters
        ----------
        p: (int)

        usage constraints
        -----------------
        self.terms is not empty
        p >= 0

        return
        ------
        (Polynomial) this polynomial powered to p
        """
        if p > 0:
            monomials = self.getMonomials()
            monoLen = len(monomials)
            if monoLen >= 2:
                half1, half2 = self.twoHalfsOfMonomials(monomials)
                poly1 = Polynomial()
                poly1.addMonomials(half1)
                poly2 = Polynomial()
                poly2.addMonomials(half2)
                res = self.binomialExpansion(poly1, poly2, p)
            else:
                singleMono = monomials[0]
                powered = singleMono.power(p)
                res = Polynomial()
                res.addMonomial(powered)
        else: 
            if not self.isNull():
                res = Polynomial()
                res.addMonomial(Monomial(1, {'': 1}))
            else:
                raise Exception("Maths error: cannot calculate 0^0")
            
        return res