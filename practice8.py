# Given data
x = [1.0, 1.5, 2.0]
y = [0.0, 0.4055, 0.6931]

n = len(x)

# Create divided difference table
dd = [[0.0 for _ in range(n)] for _ in range(n)]

# Fill first column with y values
for i in range(n):
    dd[i][0] = y[i]

# Compute divided differences
for j in range(1, n):
    for i in range(n - j):
        dd[i][j] = (dd[i + 1][j - 1] - dd[i][j - 1]) / (x[i + j] - x[i])

# Print divided difference table
print("Divided Difference Table:")
for i in range(n):
    for j in range(n - i):
        print(f"{dd[i][j]:.6f}", end="\t")
    print()

# Function to evaluate Newton Interpolation Polynomial
def newton_interpolation(val, x, dd, n):
    result = dd[0][0]
    term = 1.0

    for i in range(1, n):
        term *= (val - x[i - 1])
        result += dd[0][i] * term

    return result

# Evaluate at x = 1.7
value = 1.7
result = newton_interpolation(value, x, dd, n)

print(f"\nf({value}) = {result:.6f}")