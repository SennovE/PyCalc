from .operations import gcd, scm


class Fraction():
    """
    A class for representing fractions as numerator and denominator
    """
    __slots__ = ["numerator", "denominator"]
    __available_types = ["int", "float", "Polinominal", "Fraction"]

    def __new__(cls, numerator, denominator):
        if type(numerator).__name__ not in cls.__available_types and type(denominator) == cls.__available_types:
            raise TypeError
        
        if numerator == 0:
                return numerator
        
        instance = super(Fraction, cls).__new__(cls)

        if type(numerator) == int and type(denominator) == int:
            common_divisor = gcd(numerator, denominator)
            instance.numerator = numerator // common_divisor
            instance.denominator = denominator // common_divisor
            return instance
        
        elif type(numerator).__name__ in ["int", "Polinominal"] and type(denominator).__name__ in ["int", "Polinominal"]:            
            common_divisor = gcd(numerator, denominator)
            numerator = numerator / common_divisor
            denominator = denominator / common_divisor

            k = 1
            p = 0

            if type(numerator).__name__ == "Polinominal":
                for num in numerator.coefficients:
                    if type(numerator.coefficients[num]) == Fraction:
                        k = scm(k, numerator.coefficients[num].denominator)                        
                        p = gcd(p, int(numerator.coefficients[num].numerator))
                    elif type(numerator.coefficients[num]) in [int, float] and\
                        int(numerator.coefficients[num]) == numerator.coefficients[num]:
                        p = gcd(p, int(numerator.coefficients[num]))

            if type(denominator).__name__ == "Polinominal":
                for num in denominator.coefficients:
                    if type(denominator.coefficients[num]) == Fraction:
                        k = scm(k, denominator.coefficients[num].denominator)                        
                        p = gcd(p, int(denominator.coefficients[num].numerator))
                    elif type(denominator.coefficients[num]) in [int, float] and\
                        int(denominator.coefficients[num]) == denominator.coefficients[num]:
                        p = gcd(p, int(denominator.coefficients[num]))

            instance.numerator = numerator * abs(k) / abs(p)
            instance.denominator = denominator * abs(k) / abs(p)
            return instance
            
        elif type(numerator) == Fraction or type(denominator) == Fraction:
            return numerator / denominator
        

    @staticmethod
    def toFration(number: float|int) -> "Fraction":
        """
        A function for finding the numerator and denominator that makes a given number
        """

        if type(number) not in [int, float]:
            raise TypeError("can only convert 'float' or 'int' to Fraction with this function")
        
        if type(number) == int:
            return number

        numerator, denominator = 1, 1

        while abs(number - numerator / denominator) > 10e-20:
            if numerator > 10**3 or denominator > 10**3:
                raise Exception("number cannot be converted :(")
            if numerator / denominator < number:
                numerator += 1
            else:
                denominator += 1

        return Fraction(numerator, denominator)
    

    def __add__(self, other) -> "Fraction":
        """'Fraction' + other"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for +: '{type(other).__name__}' and 'Fraction'")
        
        elif type(other) == float:
            try:
                other = self.toFration(other)
            except Exception:
                return other + self.numerator / self.denominator
    
        if type(other) == Fraction:
            if "Polinominal" in [type(self.numerator).__name__, type(self.denominator).__name__,
                                 type(other.numerator).__name__, type(other.denominator).__name__]:
                return (self.numerator * other.denominator + self.denominator * other.numerator) / (self.denominator * other.denominator)
        
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator)
    
    __radd__ = __add__


    def __sub__(self, other):
        """'Fraction' - other"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for -: 'Fraction' and '{type(other).__name__}'")
        
        elif type(other) == float:
            try:
                other = self.toFration(other)
            except Exception:
                return self.numerator / self.denominator - other
        
        if type(other) == Fraction:
            if "Polinominal" in [type(self.numerator).__name__, type(self.denominator).__name__,
                                 type(other.numerator).__name__, type(other.denominator).__name__]:
                a = (self.numerator * other.denominator - self.denominator * other.numerator) / (self.denominator * other.denominator)
                return a
        
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator)


    def __rsub__(self, other) -> "Fraction":
        """other - 'Fraction'"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for -: '{type(other).__name__}' and 'Fraction'")
        
        elif type(other) == float:
            try:
                other = self.toFration(other)
            except Exception:
                return other - self.numerator / self.denominator
        
        if type(other) == Fraction:
            if "Polinominal" in [type(self.numerator).__name__, type(self.denominator).__name__,
                                 type(other.numerator).__name__, type(other.denominator).__name__]:
                return (self.denominator * other.numerator - self.numerator * other.denominator) / (self.denominator * other.denominator)
        
        return Fraction(self.denominator * other.numerator - self.numerator * other.denominator, self.denominator * other.denominator)
    
    

    def __mul__(self, other) -> "Fraction":
        """'Fraction' * other"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for *: '{type(other).__name__}' and 'Fraction'")
        
        elif type(other) == float:
            try:
                other = self.toFration(other)
            except Exception:
                return other * self.numerator / self.denominator
        
        if type(other) == Fraction:
            if "Polinominal" in [type(self.numerator).__name__, type(self.denominator).__name__,
                                 type(other.numerator).__name__, type(other.denominator).__name__]:
                return (self.numerator * other.numerator) / (self.denominator * other.denominator)

        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    __rmul__ = __mul__


    def __truediv__(self, other) -> "Fraction":
        """'Fraction' / other"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for /: '{type(other).__name__}' and 'Fraction'")
        
        elif type(other) == float:
            try:
                other = self.toFration(other)
            except Exception:
                return self.numerator / self.denominator / other
        
        if type(other) == Fraction:
            if "Polinominal" in [type(self.numerator).__name__, type(self.denominator).__name__,
                                 type(other.numerator).__name__, type(other.denominator).__name__]:
                return (self.numerator * other.denominator) / (self.denominator * other.numerator)
        
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        

    def __rtruediv__(self, other) -> "Fraction":
        """other / 'Fraction'"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for /: 'Fraction' and '{type(other).__name__}'")
        
        elif type(other) == float:
            try:
                other = self.toFration(other)
            except Exception:
                return  other / self.numerator * self.denominator
        
        if type(other) == Fraction:
            if "Polinominal" in [type(self.numerator).__name__, type(self.denominator).__name__,
                                 type(other.numerator).__name__, type(other.denominator).__name__]:
                return (self.denominator * other.numerator) / (self.numerator * other.numerator)
        
        return Fraction(other.numerator * self.denominator, other.denominator * self.numerator)
    

    def __pow__(self, other) -> "Fraction":
        """'Fraction' ** other"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for **: 'Fraction' and '{type(other).__name__}'")
       
        return Fraction(self.numerator**other, self.denominator**other)
    

    def __float__(self):
        return self.numerator / self.denominator
    

    def __int__(self):
        return self.numerator // self.denominator
    

    def __eq__(self, other) -> bool: # self == other        
        return abs(float(self) - float(other)) < 10**(-20)
    

    def __lt__(self, other) -> bool: # self < other
        return (float(self) - float(other)) < 0
    
    
    def __le__(self, other) -> bool: # self <= other
        return (float(self) - float(other)) <= 0
    
    
    def __gt__(self, other) -> bool: # self > other
        return (float(self) - float(other)) > 0
    
    
    def __ge__(self, other) -> bool: # self >= other
        return (float(self) - float(other)) >= 0
    
    
    def __abs__(self) -> "Fraction": # abs( self )
        return Fraction(abs(self.numerator), abs(self.denominator))
    

    def __iadd__(self, other) -> "Fraction":
        return self + other


    def __isub__(self, other) -> "Fraction":
        return self - other
    

    def __imul__(self, other) -> "Fraction":
        return self * other
    
    
    def __itruediv__(self, other) -> "Fraction":
        return self / other
    
    
    def __repr__(self) -> str:
        if self.numerator == 0 or self.denominator == 1:
            return str(self.numerator)
        elif type(self.numerator).__name__ == "Polinominal" or type(self.denominator).__name__ == "Polinominal":
            return f"({self.numerator})/({self.denominator})"
        return f"{self.numerator}/{self.denominator}"
