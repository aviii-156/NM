def f(x):
    return x**2 - 4   # example function

def regula_falsi(a, b, tol, max_iter=200):
    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return None
    c_old = a
    for i in range(max_iter):
        c = (a*f(b) - b*f(a)) / (f(b) - f(a))

        if abs(c - c_old) < tol:
            return c

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_old = c

    return c


# Function call (OUTSIDE)
root = regula_falsi(0, 3, 1e-5)
print("Approximate root:", root)
