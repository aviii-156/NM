# Newton-Raphson Method Implementation


def f(x):
    return x**2 - 4

def df(x):
    return 2*x

def newton_raphson(x0, tol, max_iter=100):
    x = x0
    print("Iter\t x_n\t\t f(x_n)\t\t Error")
    print("-" * 55)

    for i in range(1, max_iter + 1):
        x_new = x - f(x) / df(x)
        error = abs(x_new - x)

        print(f"{i}\t {x:.6f}\t {f(x):.6f}\t {error:.6f}")

        if error < tol:
            print("\nRoot found!")
            return x_new

        x = x_new

    print("\nMethod did not converge")
    return None


# Function call
root = newton_raphson(x0=3, tol=1e-6)
print("\nApproximate Root =", root)
