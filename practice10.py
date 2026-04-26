def simpson_38(f, a, b, n):
    # n must be multiple of 3
    if n % 3 != 0:
        raise ValueError("n must be a multiple of 3")

    h = (b - a) / n
    result = f(a) + f(b)

    for i in range(1, n):
        x = a + i * h

        if i % 3 == 0:
            result += 2 * f(x)
        else:
            result += 3 * f(x)

    result *= (3 * h / 8)
    return result
