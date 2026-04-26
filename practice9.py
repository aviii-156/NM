import math

def simpsons_rule(f, a, b, n):
    # Check if n is even
    if n % 2 != 0:
        raise ValueError("Number of intervals must be even.")

    h = (b - a) / n

    # Generate x and y values
    x = [a + i * h for i in range(n + 1)]
    y = [f(xi) for xi in x]

    # Apply Simpson's Rule formula
    integral = y[0] + y[-1]

    for i in range(1, n):
        if i % 2 == 0:
            integral += 2 * y[i]
        else:
            integral += 4 * y[i]

    integral *= h / 3
    return integral


# Function definition
f = lambda x: math.sin(x)

# Limits
a = 0
b = math.pi

# Number of intervals (must be even)
n = 6

# Compute result
result = simpsons_rule(f, a, b, n)

print("Approximate Integral:", result)