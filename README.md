# PyCalc
Mathematical module for python.

This module adds the ability to work with polynomials through the `Polynomial` class, which contains separate terms of different degrees and the correct fraction.

---

To start working with polynomials, you need to create a `Variable` and use it to set a polynomial.

### Example

```python
from PyCalc import Variable

x = Variable("x")

a = 1 / (x**2 - 3*x + 1)
c = (x**3 + 3*x**2 + 3*x + 1) / (x + 1)
b = (4*x**6 - 8*x**5 + 9*x**4 - x**3 + 2*x**2 - 5*x + 1) * (3*x**3 - x**2 + 2*x - 6) / (x**4 + x**2 + 84)
d = a - c + b

print(a)
print("=" * (100 + 6))
print(c)
print("=" * (100 + 6))
print(b)
print("=" * (100 + 6))
print(d)
```

#### Output

```Java
     1      
────────────
x^2 - 3x + 1
==========================================================================================================
x^2 + 2x + 1
==========================================================================================================
                                              -1620x^3 - 310x^2 + 81176x - 193458
12x^5 - 28x^4 + 31x^3 - 24x^2 - 966x + 2303 + ───────────────────────────────────
                                                        x^4 + x^2 + 84
==========================================================================================================
                                              -1620x^5 + 4551x^4 + 80486x^3 - 437295x^2 + 661550x - 193374
12x^5 - 28x^4 + 31x^3 - 25x^2 - 968x + 2302 + ────────────────────────────────────────────────────────────
                                                      x^6 - 3x^5 + 2x^4 - 3x^3 + 85x^2 - 252x + 84
```

---

## `PyCalc` & `Numpy`

The `Polynomial` class can be used together with `Numpy`.

### Example

```Python
from PyCalc import Variable
from numpy import array

x = Variable("x")

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

#### Output

```Java
[[x^2 + 1 3/2x x^2 - 7/2x]
 [8x 9 2x^3 - 21]]
```

---

This module also makes it possible to work with fractions.

Also in the file operations.py there is an implementation of the `fft algorithm`, which also allows for fast multiplication, which can be used when calculating the multiplication of polynomials that do not have huge powers or coefficients.
