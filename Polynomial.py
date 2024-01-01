from typing import Dict, Union
from LaTeXStyle import LatexStyle

class Variable():
    '''
    The class of the variable that can then be used in the equation
    '''

    def __new__(cls, symbol: str="x", latex=False) -> "Polinominal":
        if type(symbol) != str:
            raise TypeError(f"the type of the variable name should be 'str', not '{type(symbol).__name__}'")
        
        return Polinominal(coefficients={1:1}, symbol=symbol)



class Polinominal():
    __slots__ = ["coefficients", "symbol", "latex"]


    def __init__(self, coefficients: Dict[int, Union[float, int]], symbol: str="x", latex=True) -> None:
        if type(coefficients) != dict:
            raise TypeError("0")
        
        self.coefficients = {}
        self.symbol = symbol
        self.latex = latex
        
        for degree, coefficient in coefficients.items():
            if coefficient == 0:
                continue
            if type(degree) != int:
                raise TypeError("1")
            if type(coefficient) not in [int, float]:
                raise TypeError("2")
            self.coefficients[degree] = coefficient


    def __add__(self, other: Union[float, int, "Polinominal"]):
        if type(other) not in [int, float, Polinominal]:
            raise TypeError(f"unsupported operand type(s) for +: '{type(other).__name__}' and 'Polinominal'")
        
        terms = self.coefficients.copy()
        
        if type(other) in [int, float]:
            terms[0] = terms.get(0, 0) + other
        
        elif type(other) == Polinominal:
            for degree, coefficient in other.coefficients.items():
                terms[degree] = terms.get(degree, 0) + coefficient

        return Polinominal(terms, self.symbol, self.latex)
        
    __radd__ = __add__


    def __neg__(self):
        terms = {}

        for degree, coefficient in self.coefficients.items():
            terms[degree] = -coefficient

        return Polinominal(terms, self.symbol, self.latex)


    def __sub__(self, other: Union[float, int, "Polinominal"]):
        if type(other) not in [int, float, Polinominal]:
            raise TypeError(f"unsupported operand type(s) for -: 'Polinominal' and '{type(other).__name__}'")
        
        terms = self.coefficients.copy()

        if type(other) in [int, float]:
            terms[0] = terms.get(0, 0) - other
        
        elif type(other) == Polinominal:
            for degree, coefficient in other.coefficients.items():
                terms[degree] = terms.get(degree, 0) - coefficient

        return Polinominal(terms, self.symbol, self.latex)
    

    def __rsub__(self, other: Union[float, int, "Polinominal"]):
        if type(other) not in [int, float, Polinominal]:
            raise TypeError(f"unsupported operand type(s) for -: '{type(other).__name__}' and 'Polinominal'")
        
        terms = self.coefficients.copy()

        if type(other) in [int, float]:
            terms[0] = -terms.get(0, 0) + other
        
        elif type(other) == Polinominal:
            for degree, coefficient in other.coefficients.items():
                terms[degree] = -terms.get(degree, 0) + coefficient

        return Polinominal(terms, self.symbol, self.latex)


    def __mul__(self, other: Union[float, int, "Polinominal"]):
        if type(other) not in [int, float, Polinominal]: 
            raise TypeError(f"unsupported operand type(s) for *: '{type(other).__name__}' and 'Polinominal'")
        
        terms = {}

        if type(other) in [int, float]:
            other = Polinominal({0: other}, self.symbol)

        for first_degree, first_coefficient in self.coefficients.items():
            for second_degree, second_coefficient in other.coefficients.items():
                new_degree = first_degree + second_degree
                terms[new_degree] = terms.get(new_degree, 0) + first_coefficient * second_coefficient

        return Polinominal(terms, self.symbol, self.latex)

    __rmul__ = __mul__


    def __pow__(self, other: int):
        if type(other) not in [int]: 
            raise TypeError(f"unsupported operand type(s) for **: '{type(other).__name__}' and 'Polinominal'")
        if other < 0: 
            raise TypeError(f"<0")
        
        if other == 0:
            return 1
        
        new_poli = Polinominal(self.coefficients.copy(), self.symbol, self.latex)

        for _ in range(other-1):
            new_poli = new_poli * self

        return new_poli


    def __str__(self) -> str:
        terms = []
        if self.latex:
            var_symb = f"{LatexStyle.ITALIC}{self.symbol}{LatexStyle.RESET_FORMATTING}"
        else:
            var_symb = self.symbol

        degrees = sorted(self.coefficients, reverse=True)

        if len(degrees) == 0:
            return "0"

        for i in range(len(degrees)):
            term_degree = degrees[i]
            term_coefficient = self.coefficients[term_degree]

            sign, coefficient, degree = "", "", ""

            if i == 0:
                sign = "-" if term_coefficient < 0 else ""
            else:
                sign = " - " if term_coefficient < 0 else " + "

            term_coefficient = abs(term_coefficient)

            if term_degree == 0:
                coefficient = str(term_coefficient)
            else:
                coefficient = "" if term_coefficient == 1 else str(term_coefficient)

            if term_degree == 1:
                degree = var_symb
            elif term_degree != 0:
                degree = f"{var_symb}^{term_degree}" if not self.latex else\
                    f"{var_symb}{''.join(LatexStyle.UPNUMS[number] for number in str(term_degree))}"

            terms.append(sign + coefficient + degree)

        return "".join(terms)

    

if __name__ == "__main__":
    x = Variable("x", latex=True)
    first_poli = (1 + 2*x - 3*x**2)*(4 + 5*x + 6*x**2)**2
    second_poli = (-3*x**2 + 2*x + 1)*(6*x**3 + 5*x + 4)
    third_poli = -x**9999995
    print(third_poli)
