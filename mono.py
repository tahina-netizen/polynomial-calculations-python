class Monomial:
    """
    fields
    ------
    constant: (float) constant of the monomial
    variables: (dict) variables of the monomial. The key is the variable's name (str), the value is its power
    Conventionnaly, 
    "" represents 1 as a variable
    a null monomial is a monomial with a null constant
    """

    def __init__(self, const, var={'': 1}):
        """
        parameters
        ----------
        const: (float) the constant of the monomial
        var: (dict) variables of the monomial. The key is the variable's name (str), the value is its power
        
        usage constraints
        -----------------
        Do not use '' as variable name
        """
        self.constant = const
        self.variables = var
        if '' in self.variables:
            self.variables[''] = 1

    def variablesToTuple(self, reverse=False):
        """
        parameters
        ----------
        reverse: (bool)

        return
        ------
        (tuple) tuple of tuple each element is a tuple having this structure: (variable's name (str), its power (int)
        """
        varNames = list(self.variables.keys())
        varNames.sort(reverse=reverse)
        res = []
        for v in varNames:
            res.append((v, self.variables[v]))
        return tuple(res)

    def multiply(self, mono):
        """
        parameters
        ----------
        mono: (Monomial)

        return
        ------
        (Monomial) this monomial multiplied by <mono>
        multiplying with a null Monomial will give a null Monomial
        """
        const = self.constant * mono.constant
        
        if const == 0:
            variables = {'': 1}
        else:
            variables = self.variables.copy()
            variables.pop("", None)
            for name in mono.variables:
                if name != "":
                    if name in variables:
                        variables[name] += mono.variables[name]
                    else:
                        variables[name] = mono.variables[name]
            if variables == {}:
                variables[''] = 1
        return Monomial(const, variables)

    def isNull(self):
        """
        return
        ------
        (bool) true if this is a null monomial, else Fase
        """
        return self.constant == 0

    def variablesToStr(self):
        """
        return
        ------
        (str) string representation of variables and its powers
        """
        varNames = list(self.variables.keys())
        varNames.sort()
        res = []
        for name in varNames:
            if name != "":
                res.append(name)
                res.append(str(self.variables[name]))
        return "".join(res)

    def power(self, p):
        """
        parameters
        ----------
        p: (int)

        usage constraints
        -----------------
        p >= 0

        return
        ------
        (Monomial) this monomial powered <p>
        """
        if not self.isNull():
            if p > 0:
                const = self.constant ** p
                variables = self.variables.copy()
                variables.pop('', None) # 1 does not make any change after powering
                for name in variables:
                    variables[name] *= p
                if variables == dict():
                    variables[''] =  1
                res = Monomial(const, variables)
            else: 
                res = Monomial(1)
        else:
            if p > 0:
                res = Monomial(0)
            else:
                raise Exception("Maths error: cannot calculate 0^0")
        return res

    def toString(self):
        """
        return
        ------
        (str) a string representation
        """
        v = self.variablesToStr()
        if self.constant >= 0:
            c = "+"+str(self.constant)
        else:
            c = str(self.constant)
        res = "{} {} ".format(c, v)
        return res
