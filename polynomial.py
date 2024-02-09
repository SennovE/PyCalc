from typing import Dict, Union
from .fraction import Fraction


class Variable():
    """
    #### The class of the variable that can then be used in the mathematical expression

    ##### Usage:

    ```Python
    x = Variable("x")
    expression = 2*x**2 + x + 1 + (x + 4) / (x**3)
    ```
    """

    def __new__(cls, symbol: str="x"):
        if type(symbol) != str:
            raise TypeError(f"the type of the variable name should be 'str', not '{type(symbol).__name__}'")
        
        return Polinominal(coefficients={1:1}, symbol=symbol)


class Polinominal():
    """
    A class for representing a polynomial as a separate terms of different degrees and the correct fraction.

    To make mathematical expression use `Variable` class.
    """
    __slots__ = ["coefficients", "symbol", "fraction"]

    def __init__(self, coefficients: Dict[int, Union[float, int, Fraction]]={}, fraction: Fraction=0, symbol: str="x") -> None:
        if type(coefficients) != dict:
            raise TypeError("use the Variable class to create a variable, and then make an expression")
        
        self.coefficients = {0: 0}
        self.symbol = symbol
        self.fraction = fraction
        
        for degree, coefficient in coefficients.items():
            if degree != 0 and coefficient == 0:
                continue
            if type(degree) != int:
                raise TypeError
            if type(coefficient) not in [int, float, Fraction]:
                raise TypeError
            if type(coefficient) == Fraction:
                if coefficient.numerator == 0:
                    continue
                self.coefficients[degree] = coefficient
            else:
                if int(coefficient) == coefficient:
                    self.coefficients[degree] = Fraction(int(coefficient), 1)
                else:                    
                    self.coefficients[degree] = Fraction(coefficient, 1)


    def __add__(self, other: Union[float, int, "Polinominal", Fraction]) -> "Polinominal":
        """ 'Polinominal' + other """

        if type(other) not in [int, float, Polinominal, Fraction]:
            raise TypeError(f"unsupported operand type(s) for +: '{type(other).__name__}' and 'Polinominal'")
        
        terms = self.coefficients.copy()
        fraction = self.fraction
        
        if type(other) in [int, float]:
            terms[0] = terms.get(0, 0) + other

        elif type(other) == Fraction:
            fraction = fraction + other
        
        elif type(other) == Polinominal:
            frac_poli: Polinominal = self.fraction + other.fraction
            for degree, coefficient in other.coefficients.items():
                terms[degree] = terms.get(degree, 0) + coefficient
            if type(frac_poli) == Polinominal:
                for degree, coefficient in frac_poli.coefficients.items():
                    terms[degree] = terms.get(degree, 0) + coefficient
                fraction = frac_poli.fraction
            elif type(frac_poli) == Fraction:
                fraction = frac_poli

        return Polinominal(terms, symbol=self.symbol, fraction=fraction)
        
    __radd__ = __add__


    def __neg__(self) -> "Polinominal":
        """ -'Polinominal' """

        terms = {}

        for degree, coefficient in self.coefficients.items():
            terms[degree] = -coefficient

        return Polinominal(terms, symbol=self.symbol, fraction=self.fraction*(-1))


    def __sub__(self, other: Union[float, int, "Polinominal", Fraction]) -> "Polinominal":
        """ 'Polinominal' - other """

        if type(other) not in [int, float, Polinominal, Fraction]:
            raise TypeError(f"unsupported operand type(s) for -: 'Polinominal' and '{type(other).__name__}'")
        
        terms = self.coefficients.copy()
        fraction = self.fraction

        if type(other) in [int, float]:
            terms[0] = terms.get(0, 0) - other

        elif type(other) == Fraction:
            fraction = fraction - other

        elif type(other) == Polinominal:
            frac_poli: Polinominal = self.fraction - other.fraction
            for degree, coefficient in other.coefficients.items():
                terms[degree] = terms.get(degree, 0) - coefficient
            if type(frac_poli) == Polinominal:
                for degree, coefficient in frac_poli.coefficients.items():
                    terms[degree] = terms.get(degree, 0) + coefficient
                fraction = frac_poli.fraction
            elif type(frac_poli) == Fraction:
                fraction = frac_poli

        return Polinominal(terms, symbol=self.symbol, fraction=fraction)
    

    def __rsub__(self, other: Union[float, int, "Polinominal"]) -> "Polinominal":
        """ other - 'Polinominal' """

        if type(other) not in [int, float, Polinominal]:
            raise TypeError(f"unsupported operand type(s) for -: '{type(other).__name__}' and 'Polinominal'")        

        return (self - other) * (-1)


    def __mul__(self, other: Union[float, int, "Polinominal", Fraction]) -> "Polinominal":
        """ 'Polinominal' * other """

        if type(other) not in [int, float, Polinominal, Fraction]: 
            raise TypeError(f"unsupported operand type(s) for *: '{type(other).__name__}' and 'Polinominal'")
        
        if type(other) in [int, float, Fraction]:
            new_poli = Polinominal(self.coefficients, symbol=self.symbol)
            for i in new_poli.coefficients:
                new_poli.coefficients[i] = new_poli.coefficients[i] * other
            new_poli.fraction = self.fraction * other
            return new_poli
        
        terms = {}
        if not (self.fraction or other.fraction):
            for first_degree, first_coefficient in self.coefficients.items():
                for second_degree, second_coefficient in other.coefficients.items():
                    new_degree = first_degree + second_degree
                    terms[new_degree] = terms.get(new_degree, 0) + first_coefficient * second_coefficient
            return Polinominal(terms, symbol=self.symbol)
        
        else:
            self_numer = 0
            self_denom = 1
            other_numer = 0
            other_denom = 1
            if self.fraction:
                self_numer = self.fraction.numerator
                self_denom = self.fraction.denominator
            if other.fraction:
                other_numer = other.fraction.numerator
                other_denom = other.fraction.denominator

            return (Polinominal(self.coefficients, symbol=self.symbol) * self_denom + self_numer) * \
                   (Polinominal(other.coefficients, symbol=self.symbol) * other_denom + other_numer) / \
                   (self_denom * other_denom)
        

    __rmul__ = __mul__


    def __pow__(self, other: int) -> "Polinominal":
        """ 'Polinominal' ** other """

        if type(other) not in [int]: 
            raise TypeError(f"unsupported operand type(s) for **: '{type(other).__name__}' and 'Polinominal'")
        if other < 0: 
            raise TypeError(f"the degree of the number must not be lower than 0")
        
        if other == 0:
            return 1
        
        new_poli = Polinominal(self.coefficients.copy(), symbol=self.symbol)

        for _ in range(other-1):
            new_poli = new_poli * self

        return new_poli
    
    
    def __truediv__(self, other: Union[int, float, "Polinominal", Fraction]) -> "Polinominal":
        """ 'Polinominal' / other """

        if type(other) not in [int, float, Polinominal, Fraction]:
            raise TypeError(f"unsupported operand type(s) for /: '{type(other).__name__}' and 'Polinominal'")        

        old_poli = self.coefficients.copy()

        if type(other) in [int, float, Fraction]:
            for i in old_poli:
                old_poli[i] /= other
            return Polinominal(old_poli, symbol=self.symbol, fraction=self.fraction / other)

        fraction = 0
        if self.fraction:
            fraction = self.fraction / other

        new_poli = Polinominal({}, symbol=self.symbol, fraction=fraction)
        old_poli = Polinominal(old_poli, symbol=self.symbol)

        while old_poli.coefficients != {0: 0} and max(old_poli.coefficients) >= max(other.coefficients):
            multiplier = Polinominal(
                {max(old_poli.coefficients) - max(other.coefficients):
                Fraction(old_poli.coefficients[max(old_poli.coefficients)], other.coefficients[max(other.coefficients)])},
                symbol=self.symbol)
            tmp = multiplier * other
            new_poli = new_poli + multiplier
            old_poli = old_poli - tmp

        
        if old_poli.coefficients != {0: 0}:
            new_poli.fraction += Fraction(old_poli, other)

        return new_poli
                

    def __rtruediv__(self, other: Union[int, float, "Polinominal", Fraction]) -> "Polinominal":
        """ other / 'Polinominal' """

        if type(other) not in [int, float, Polinominal, Fraction]:
            raise TypeError(f"unsupported operand type(s) for /: '{type(other).__name__}' and 'Polinominal'")
        
        if self.fraction:
            self_numerator = self.fraction.denominator
            self_denominator = self.fraction.numerator + Polinominal(self.coefficients, symbol=self.symbol) * self.fraction.denominator
        else:
            self_numerator = 1
            self_denominator = Polinominal(self.coefficients, symbol=self.symbol)

        if type(other) in [int, float]:
            other = Polinominal({0: other})
        
        if other.fraction:
            other_denominator = other.fraction.denominator
            other_numerator = other.fraction.numerator + Polinominal(other.coefficients, symbol=self.symbol) * other.fraction.denominator
        else:
            other_denominator = 1
            other_numerator = Polinominal(other.coefficients, symbol=self.symbol)

        return (self_numerator * other_numerator) / (self_denominator * other_denominator)


    def __mod__(self, other: Union[int, float, "Polinominal", Fraction]) -> "Polinominal":
        """ 'Polinominal' % other """

        if type(other) not in [int, float, Polinominal, Fraction]:
            raise TypeError(f"unsupported operand type(s) for %: '{type(other).__name__}' and 'Polinominal'")        

        old_poli = self.coefficients.copy()

        if type(other) in [int, float, Fraction]:
            for i in old_poli:
                old_poli[i] /= other
            return Polinominal(old_poli, symbol=self.symbol)
            
        old_poli = Polinominal(old_poli, symbol=self.symbol)

        while old_poli.coefficients != {0: 0} and max(old_poli.coefficients) >= max(other.coefficients):
            multiplier = Polinominal(
                {max(old_poli.coefficients) - max(other.coefficients):
                Fraction(old_poli.coefficients[max(old_poli.coefficients)], other.coefficients[max(other.coefficients)])},
                symbol=self.symbol)
            tmp = multiplier * other
            old_poli = old_poli - tmp

        if old_poli.coefficients != {0: 0}:
            return old_poli

        return 0

                        
    def __str__(self) -> str:

        def makeFrac(numer: str, denom: str) -> list[str]:
            if len(denom) > len(numer):
                numer = ((len(denom) - len(numer)) // 2) * " " + numer + ((len(denom) - len(numer)) // 2 + (len(denom) - len(numer)) % 2) * " "
                divider = "─" * len(denom)

            else:                
                denom = ((len(numer) - len(denom)) // 2) * " " + denom + ((len(numer) - len(denom)) // 2 + (len(numer) - len(denom)) % 2) * " "
                divider = "─" * len(numer)
            
            return [str(numer), str(divider), str(denom)]
       
        var_symb = self.symbol
        
        terms_numer = []
        terms_mid = []
        terms_denom = []
        frac = False

        degrees = sorted(self.coefficients, reverse=True)

        if (len(degrees) == 0 or self.coefficients == {0: 0}) and not self.fraction:
            return "0"
        for i in range(len(degrees)):
            term_degree = degrees[i]
            term_coefficient = self.coefficients[term_degree]
            if term_coefficient == 0:
                continue
            
            sign, degree = "", ""
            
            if i == 0:
                sign = "-" if term_coefficient < 0 else ""
            else:
                sign = " - " if term_coefficient < 0 else " + "

            term_coefficient = abs(term_coefficient)

            if term_degree == 0:
                if type(term_coefficient) == Fraction:
                    if term_coefficient.denominator == 1:
                        mid = str(term_coefficient.numerator)
                        numer = denom = " " * len(mid)
                    else:
                        frac = True
                        numer, mid, denom = makeFrac(str(term_coefficient.numerator), str(term_coefficient.denominator))
                else:                    
                    mid = str(term_coefficient)
                    numer = denom = " " * len(mid)

            else:
                if term_coefficient == 1:
                    numer, mid, denom = "", "", ""
                else:
                    if type(term_coefficient) == Fraction:
                        if term_coefficient.denominator == 1:
                            mid = str(term_coefficient.numerator)
                            numer = denom = " " * len(mid)
                        else:
                            frac = True
                            numer, mid, denom = makeFrac(str(term_coefficient.numerator), str(term_coefficient.denominator))
                    else:
                        mid = str(term_coefficient)
                        numer = denom = " " * len(mid)

            if term_degree == 1:
                degree = var_symb
            elif term_degree != 0:
                degree = f"{var_symb}^{term_degree}"

            mid = sign + mid + degree
            numer = " " * len(sign) + numer + " " * (len(mid) - len(sign) - len(numer))
            denom = " " * len(sign) + denom + " " * (len(mid) - len(sign) - len(denom))
        
            terms_numer.append(numer)
            terms_mid.append(mid)
            terms_denom.append(denom)

        terms_numer = "".join(terms_numer)
        terms_mid = "".join(terms_mid)
        terms_denom = "".join(terms_denom)

        if self.fraction:
            frac = True
            numer, divider, denom = makeFrac(repr(self.fraction.numerator), repr(self.fraction.denominator))

            if terms_mid:
                terms_numer = terms_numer + " " * 3 + numer
                terms_mid = terms_mid + " + " + divider
                terms_denom = terms_denom + " " * 3 + denom
            else:
                terms_numer = numer
                terms_mid = divider
                terms_denom = denom


        if frac:
            return f"{terms_numer}\n{terms_mid}\n{terms_denom}"        
        return terms_mid
        
        
    def __repr__(self) -> str:
        string = []
        var_symb = self.symbol
        degrees = sorted(self.coefficients, reverse=True)
        for i in degrees:
            s = ""

            if self.coefficients[i] == 0:
                continue

            if i == degrees[0]:
                s = "-" if self.coefficients[i] < 0 else ""
            else:
                s = "- " if self.coefficients[i] < 0 else "+ "


            if abs(self.coefficients[i]) != 1 or i == 0:
                s += str(abs(self.coefficients[i]))

            if i == 1:
                s += var_symb
            elif i != 0:
                s += f"{var_symb}^{i}"
            string.append(s)
                
        if self.fraction:
            if len(string) != 0:
                string.append(f"+ ({repr(self.fraction.numerator)})/({repr(self.fraction.denominator)})")
            else:                
                string.append(f"({repr(self.fraction.numerator)})/({repr(self.fraction.denominator)})")

        if len(string) == 0:
            return "0"
        
        return " ".join(string)
    

    def evaluate_polynomial(self, variable: Union[int, float, Fraction]):
        value = 0
        for degree in self.coefficients:
            value += self.coefficients[degree] * variable ** degree
        if self.fraction:
            value += (self.fraction.numerator.evaluate_polynomial(variable) / self.fraction.denominator.evaluate_polynomial(variable))
        return value