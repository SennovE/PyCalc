"""
# PyCalc

This module adds the ability to work with polynomials through the `Polynomial` class, which contains separate terms of different degrees and the correct fraction.

## Getting started

To start working with polynomials, you need to create a `Variable` and use it to set a polynomial.

Example

```
from PyCalc import Variable
x = Variable("x")
expression = 2*x**2 + x + 1 + (x + 4) / (x**3)
```
"""

from .polynomial import Variable
from .fraction import *
from .operations import *