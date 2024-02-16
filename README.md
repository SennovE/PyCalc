# PyCalc
Mathematical module for python.

This module adds the ability to work with polynomials through the `Polynomial` class, which contains separate terms of different degrees and the correct fraction.

## Getting started

To start working with polynomials, you need to create a `Variable` and use it to set a mathematical expression.

<details>
<summary><h3><i>Example</i></h3></summary>

```python
from PyCalc.polynomial import Variable

x = Variable("x")

a = 1 / (x**2 - 3*x + 1)
b = (x**3 + 3*x**2 + 3*x + 1) / (x + 1)
c = (4*x**6 - 8*x**5 + 9*x**4 - x**3 + 2*x**2 - 5*x + 1) * (3*x**3 - x**2 + 2*x - 6) / (x**4 + x**2 + 84)
d = a - b + c

print(a)
print()
print(b)
print()
print(c)
print()
print(d)
```

#### Output:

```Java
     1      
────────────
x^2 - 3x + 1

x^2 + 2x + 1

                                              -1620x^3 - 310x^2 + 81176x - 193458
12x^5 - 28x^4 + 31x^3 - 24x^2 - 966x + 2303 + ───────────────────────────────────
                                                        x^4 + x^2 + 84


                                              -1620x^5 + 4551x^4 + 80486x^3 - 437295x^2 + 661550x - 193374
12x^5 - 28x^4 + 31x^3 - 25x^2 - 968x + 2302 + ────────────────────────────────────────────────────────────
                                                      x^6 - 3x^5 + 2x^4 - 3x^3 + 85x^2 - 252x + 84
```
</details>

## `PyCalc` & `Numpy`

The `Polynomial` class can be used together with `Numpy`.

<details>
<summary><h3><i>Example</i></h3></summary>

```Python
from PyCalc.polynomial import Variable
from numpy import array

x = Variable("y")

a = array([
    [1, x/2],
    [2*x, 3]
])
b = array([
    [1, 0, x**2],
    [2*x, 3, -7]
])

print(a @ b)
```

#### Output:

```Java
[[y^2 + 1 3/2y y^2 - 7/2y]
 [8y 9 2y^3 - 21]]
```
</details>

## Other features



1. This module makes it possible to work with fractions.

    You can use 'float' type in your expression and `Fraction` will automatically convert it to fraction if the numerator and denominator do not exceed <b>10^3</b> (if you don't need polynominal, you can use `Fraction.toFration('float')`).

     <details>
     <summary><h3><i>Example</i></h3></summary>
         
     ```Python
     from PyCalc.polynomial import Variable
     
     x = Variable("a")
     
     a = 125 / 387
     b = a * x
     
     print(a)
     print()
     print(b)
     ```
     
     #### Output:
     
     ```Java
     0.32299741602067183
     
     125 
     ───a
     387 
     ```
     </details>

1. `expression.evaluate_polynomial(var)` is used to substitute a value instead of a variable in an expression

     <details>     
     <summary><h3><i>Example</i></h3></summary>
          
     ```Python
     from PyCalc.polynomial import Variable
     
     x = Variable("a")
     
     a = 1 / (x**2 - 3*x + 1) + (x**3 + 3*x**2 + 3*x + 1) / (x + 1)
     
     print(a)
     print("=", (a).evaluate_polynomial(2))
     ```
     
     #### Output:
     
     ```Java
                        1      
     a^2 + 2a + 1 + ────────────
                    a^2 - 3a + 1
     = 8
     ```
     </details>

1. Also, in the submodule `operations` there is an implementation of the `fft algorithm`, which also allows for fast multiplication, which can be used when calculating the multiplication of polynomials that do not have huge powers or coefficients.

