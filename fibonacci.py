# Program fibonacci sequence using recursive and nonrecursive method
# Fibonacci nubers start with F0 = 0 and F1 = 1
# each subsequent fibonacci number is a sum of two previous

def fibo_recursive(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    if n > 1:
        return fibo_recursive(n-1) + fibo_recursive(n-2)

res = fibo_recursive(19)
print(res)

# what is the problem with recursive fibo?
#1 it is limited by computer maximum stack calls 1000
#2 repeated calls and memory for the same #
#  fibo of 99 calls fibo of 98 and fibo of 97
# fibo of 98 calls fibo of 97 and fibo of 96 (duplication of the same calls)

# please write non recursive version of fibo

def fibo_regular(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev1 = 0
    prev2 = 1
    next = 1
    if n > 1:
        for i in range(n - 1):
            next = prev1 + prev2
            prev1 = prev2
            prev2 = next
    return next

res1 = fibo_regular(19)
print(res1)