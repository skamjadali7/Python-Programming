#Finding Factorial using recursive function
#Recursive function is used for reduce code length and improve readability

def factorial(n):
    if n==0:
        result= 1
    else:
        result=n*factorial(n-1)
    return result

print(factorial(0))
print(factorial(5))