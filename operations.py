from typing import List
from cmath import exp, pi
from math import ceil, log2


def gcd(a: int, b: int) -> int:
    if type(a) != int or type(b) != int:
        raise TypeError(f"can't calculate gcd of '{type(a)}' and '{type(b)}'")    
    while a % b:
        a, b = b, a % b
    return b


def fft(x: list) -> list[complex]:
    if len(x) <= 1:
        return x
    
    N = int(2 ** ceil(log2(len(x))))
    x += [0] * (N - len(x))
    
    even = fft(x[0::2])
    odd = fft(x[1::2])

    T = [exp(-2j * pi * k / N) * odd[k] for k in range(N // 2)]

    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]


def ifft(x: list[complex]) -> list[complex]:    
    if len(x) == 1:
        return x
    
    N = int(2 ** ceil(log2(len(x))))
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


def elem_mul(a: list, b: list):
    final = []
    for i in range(len(a)):
        final.append(a[i] * b[i])
    return final


def omega(n: int):
    final = []
    for i in range(n//2):
        final.append(exp(2j * pi / n) ** i)
    
    return final


def fft_mul(poly1: list, poly2: list) -> list[complex]:
    n = int(2 ** ceil(log2(len(poly1) + len(poly2))))
    poly1 += [0] * (n - len(poly1))
    poly2 += [0] * (n - len(poly2))

    fft_poly1 = fft(poly1)
    fft_poly2 = fft(poly2)


    fft_result = elem_mul(fft_poly1, fft_poly2)

    result = ifft(fft_result)

    return result
