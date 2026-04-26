# #bisection method   
# #define function 
# def f(x):
#     return x**2-4
# #bisection method with iteration table 
# def bisection(a,b,tol):
#     if f(a)*f(b)>=0:
#         print("Bisection method fails.")
#         return None

#     iteration=1

        
#     print("Iter\t a\t b\t c\t f(c)\t Error")
#     print("_" *75)
#     while(b-a)/2>tol:
#         c=(a+b)/2
#         error=abs(b-a)/2
#         #print iteration values 
#         print(f"{iteration}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}\t {error:.6f}")
#         if f(c)==0:
#             break
#         elif f(a)*f(c)<0:
#             b=c
#         else:
#             a=c
#         iteration+=1
#     return (a+b)/2
# #input interval and tolerance
# root =bisection(0,3,1e-2)
# print("\nApproximate root: ",root)

#question 
# find the root of f(x)=x^3-x-2 using bisection method in the interval [1,2] 
# #bisection method   
#define function 
def f(x):
    return x**3-x-2
#bisection method with iteration table 
def bisection(a,b,tol):
    if f(a)*f(b)>=0:
        print("Bisection method fails.")
        return None

    iteration=1

        
    print("Iter\t a\t b\t c\t f(c)\t Error")
    print("_" *75)
    while(b-a)/2>tol:
        c=(a+b)/2
        error=abs(b-a)/2
        #print iteration values 
        print(f"{iteration}\t {a:.6f}\t {b:.6f}\t {c:.6f}\t {f(c):.6f}\t {error:.6f}")
        if f(c)==0:
            break
        elif f(a)*f(c)<0:
            b=c
        else:
            a=c
        iteration+=1
    return (a+b)/2
#input interval and tolerance
root =bisection(1,2,1e-3)
print("\nApproximate root: ",root)






#question
#problem statement : find a root f(x)=e^{-x} -x using bisection method in the interval [0,1]

# Taylor Series for exp(x)
# import math

# def taylor_exp(x, n):
#     result = 0.0
#     for i in range(n):
#         result += (x ** i) / math.factorial(i)
#     return result

# x_exp = 1.0
# term_list = [2, 4, 6, 8]

# print("Truncation Error Analysis for exp(x)\n")

# true_exp = math.exp(x_exp)

# for n in term_list:
#     approx_exp = taylor_exp(x_exp, n)
#     error = abs(true_exp - approx_exp)

#     print(f"Terms: {n}, Approx exp: {approx_exp}, True exp: {true_exp}, Truncation error: {error}")
