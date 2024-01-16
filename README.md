# PyCalc
Mathematical module for python

This module adds the ability to work with polynomials through the `Polynomial` class, which contains separate terms of different degrees and the correct fraction.

To start working with polynomials, you need to create a `Variable` and use it to set a polynomial.

### Example

```python
from polinominal import Variable

x = Variable("x")
poli = (-3 * x**2 + 2 * x + 1) * (6 * x**3 + 5 * x + 4)
print(poli)

# output
# -18x^5 + 12x^4 - 9x^3 - 2x^2 + 13x + 4
```

This module also makes it possible to work with fractions.

Also in the file operations.py there is an implementation of the `fft algorithm`, which also allows for fast multiplication, which can be used when calculating the multiplication of polynomials that do not have huge powers or coefficients.