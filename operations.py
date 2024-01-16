from typing import List
from cmath import exp, pi
import numpy as np


def gcd(a: int, b: int) -> int:
    if type(a) != int or type(b) != int:
        raise TypeError(f"can't calculate gcd of '{type(a)}' and '{type(b)}'")    
    while a % b:
        a, b = b, a % b
    return b


def fft(x):
    if len(x) <= 1:
        return x
    
    N = int(2 ** np.ceil(np.log2(len(x))))
    x += [0] * (N - len(x))
    
    even = fft(x[0::2])
    odd = fft(x[1::2])

    T = [exp(-2j * pi * k / N) * odd[k] for k in range(N // 2)]

    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]


def ifft(x):    
    if len(x) == 1:
        return x
    
    N = int(2 ** np.ceil(np.log2(len(x))))
    x += [0] * (N - len(x))
    
    omega_N = exp(2j * pi / N)

    even = ifft(x[::2])
    odd = ifft(x[1::2])

    factor = omega(N)

    factor = elem_mul(factor, odd)

    x = []
    
    for i in range(len(even)):
        x.append((factor[i] + even[i]) / 2)
    for i in range(len(even)):
        x.append((even[i] - factor[i]) / 2)
    
    return x


def elem_mul(a, b):
    final = []
    for i in range(len(a)):
        final.append(a[i] * b[i])
    return final


def omega(n):
    final = []
    for i in range(n//2):
        final.append(exp(2j * pi / n) ** i)
    
    return final


def fft_mul(poly1, poly2):
    poly1 = [poly1.coefficients.get(i, 0) for i in range(max(poly1.coefficients) + 1)]
    poly2 = [poly2.coefficients.get(i, 0) for i in range(max(poly2.coefficients) + 1)]

    n = int(2 ** np.ceil(np.log2(len(poly1) + len(poly2))))
    poly1 += [0] * (n - len(poly1))
    poly2 += [0] * (n - len(poly2))

    fft_poly1 = fft(poly1)
    fft_poly2 = fft(poly2)


    fft_result = elem_mul(fft_poly1, fft_poly2)
    print([round(i.real) for i in ifft(fft(poly1))[:10]])
    print(poly1[:10])

    result = ifft(fft_result)

    terms = {}

    for i in range(len(result)):
        if result[i] != 0:
            terms[i] = round(result[i].real, 2)

    return terms
