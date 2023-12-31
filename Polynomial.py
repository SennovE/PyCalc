from typing import Dict, Union

class Variable():
    '''
    The class of the variable that can then be used in the equation
    '''
    __slots__ = ["symbol"]


    def __init__(self, symbol: str="x") -> None:
        if type(symbol) != str:
            raise TypeError(f"the type of the variable name should be 'str', not '{type(symbol).__name__}'")
        
        self.symbol = symbol


    def __str__(self) -> str:
        return self.symbol 

    
    def __mul__(self, other: Union[float, int, "Variable", "Polinominal"]):
        if type(other) not in [int, float, Variable, Polinominal]:
            raise TypeError(f"can't multiply 'Variable' with '{type(other).__name__}'")
        
        if type(other) in [int, float]:
            return Polinominal({1: other})
        
        elif type(other) == Polinominal:
            new_poli = {}
            for degree, coefficient in other.coefficients.items():
                new_poli[degree + 1] = coefficient
            return Polinominal(new_poli)
        
        elif type(other) == Variable:
            return Polinominal({2: 1})

    __rmul__ = __mul__


class Polinominal():
    __slots__ = ["coefficients"]


    def __init__(self, coefficients: Dict[int, Union[float, int]]) -> None:
        if type(coefficients) != dict:
            raise TypeError("0")
        
        self.coefficients = {}
        
        for degree, coefficient in coefficients.items():
            if type(degree) != int:
                raise TypeError("1")
            if type(coefficient) not in [int, float]:
                raise TypeError("2")
            self.coefficients[degree] = coefficient
    

    def __str__(self) -> str:
        terms = []
        var_symb = "x"
        
        for degree in sorted(self.coefficients, reverse=True):
            coefficient = self.coefficients[degree]
            if coefficient == 0:
                continue

            if degree == 1:
                if coefficient == 1:
                    terms.append(str(f"{var_symb}"))
                else:
                    terms.append(str(f"{coefficient}{var_symb}"))

            elif degree == 0:
                terms.append(str(f"{coefficient}"))

            else:
                if coefficient == 1:
                    terms.append(str(f"{var_symb}^{degree}"))
                else:
                    terms.append(str(f"{coefficient}{var_symb}^{degree}"))                

        if len(terms) == 0:
            return "0"
        return " + ".join(terms)

    


x = Variable("x")
p = x * 0
print(p)
