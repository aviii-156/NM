# 
# absolute and relative error example
# true=3.14159
# aprox=3.14
# abs_error=abs(true-aprox)
# rel_error=abs_error/true
# print("Absolute Error:", abs_error)
# print("Relative Error:", rel_error)


# round-off error example
# from decimal import Decimal
# sum_value= Decimal(0.0)
# for i in range(10):
#     sum_value += Decimal('0.1')
# print("Sum:", sum_value)
# print("Expacted vale=",Decimal('1.0'))
# print("error=", sum_value-Decimal('1.0'))


# truncation error example

# import math
# x=math.pi/6
# true_value=math.sin(x)
# aprox_value=x-x**3/math.factorial(3)
# print("True value:", true_value)
# print("Approx value:", aprox_value)
# print("truncation error", abs(true_value - aprox_value))


import math

def taylor_exp(x, n):
    result = 0.0
    for i in range(n):
        result += (x ** i) / math.factorial(i)
    return result


x_exp = 1.0
term_list = [2, 4, 6, 8]

print("Truncation Error Analysis for exp(x)\n")

true_exp = math.exp(x_exp)

for n in term_list:
    approx_exp = taylor_exp(x_exp, n)
    error = abs(true_exp - approx_exp)
    
    print(f"Terms: {n}, Approx exp: {approx_exp}, True exp: {true_exp}, Truncation error: {error}")
