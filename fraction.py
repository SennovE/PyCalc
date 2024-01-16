from operations import gcd


class Fraction():
    """
    A class for representing fractions as numerator and denominator
    """
    __slots__ = ["numerator", "denominator"]
    __available_types = ["int", "float", "Polinominal", "Fraction"]

    def __init__(self, numerator, denominator) -> None:
        if type(numerator) == int and type(denominator) == int:
            common_divisor = gcd(numerator, denominator)
            self.numerator = numerator // common_divisor
            self.denominator = denominator // common_divisor
        
        elif type(numerator).__name__ in ["int", "Polinominal"] and type(denominator).__name__ in ["int", "Polinominal"]:         
            self.numerator = numerator
            self.denominator = denominator

        else:
            print(type(numerator), type(denominator))
            raise TypeError


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

        while abs(number - numerator / denominator) > 10e-20 :
            if numerator / denominator < number:
                numerator += 1
            else:
                denominator += 1

        return Fraction(numerator, denominator)
    

    def __add__(self, other) -> "Fraction":
        """'Fraction' + other"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for +: '{type(other).__name__}' and 'Fraction'")
    
        elif type(other) == Fraction:
            if "Polinominal" in [type(self.numerator).__name__, type(self.denominator).__name__,
                                 type(other.numerator).__name__, type(other.denominator).__name__]:
                return (self.numerator * other.denominator + self.denominator * other.numerator) / (self.denominator * other.denominator)
        
        return Fraction(self.numerator * other.denominator + self.denominator * other.numerator, self.denominator * other.denominator)
    
    __radd__ = __add__


    def __sub__(self, other) -> "Fraction":
        """'Fraction' - other"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for -: 'Fraction' and '{type(other).__name__}'")
        
        elif type(other) == Fraction:
            if "Polinominal" in [type(self.numerator).__name__, type(self.denominator).__name__,
                                 type(other.numerator).__name__, type(other.denominator).__name__]:
                return (self.numerator * other.denominator - self.denominator * other.numerator) / (self.denominator * other.denominator)
        
        return Fraction(self.numerator * other.denominator - self.denominator * other.numerator, self.denominator * other.denominator)


    def __rsub__(self, other) -> "Fraction":
        """other - 'Fraction'"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for -: '{type(other).__name__}' and 'Fraction'")
        
        elif type(other) == Fraction:
            if "Polinominal" in [type(self.numerator).__name__, type(self.denominator).__name__,
                                 type(other.numerator).__name__, type(other.denominator).__name__]:
                return (self.denominator * other.numerator - self.numerator * other.denominator) / (self.denominator * other.denominator)
        
        return Fraction(self.denominator * other.numerator - self.numerator * other.denominator, self.denominator * other.denominator)
    
    

    def __mul__(self, other) -> "Fraction":
        """'Fraction' * other"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for *: '{type(other).__name__}' and 'Fraction'")
        
        elif type(other) == Fraction:
            if "Polinominal" in [type(self.numerator).__name__, type(self.denominator).__name__,
                                 type(other.numerator).__name__, type(other.denominator).__name__]:
                return (self.numerator * other.numerator) / (self.denominator * other.denominator)

        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    __rmul__ = __mul__


    def __truediv__(self, other) -> "Fraction":
        """'Fraction' / other"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for /: '{type(other).__name__}' and 'Fraction'")
        
        elif type(other) == Fraction:
            if "Polinominal" in [type(self.numerator).__name__, type(self.denominator).__name__,
                                 type(other.numerator).__name__, type(other.denominator).__name__]:
                return (self.numerator * other.denominator) / (self.denominator * other.numerator)
        
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)
        

    def __rtruediv__(self, other) -> "Fraction":
        """other / 'Fraction'"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for /: 'Fraction' and '{type(other).__name__}'")
        
        elif type(other) == Fraction:
            if "Polinominal" in [type(self.numerator).__name__, type(self.denominator).__name__,
                                 type(other.numerator).__name__, type(other.denominator).__name__]:
                return (self.denominator * other.numerator) / (self.numerator * other.numerator)
        
        return Fraction(other.numerator * self.denominator, other.denominator * self.numerator)
    

    def __pow__(self, other) -> "Fraction":
        """'Fraction' ** other"""

        if type(other).__name__ not in Fraction.__available_types:
            raise TypeError(f"unsupported operand type(s) for **: 'Fraction' and '{type(other).__name__}'")
       
        return Fraction(self.numerator**other, self.denominator**other)
    

    def __str__(self) -> str:
        return f"{self.numerator} / {self.denominator}"
    