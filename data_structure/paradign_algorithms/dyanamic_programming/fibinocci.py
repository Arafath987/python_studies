def fib(n, memo={}):
    if n <= 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


def fib1(n):
    if n <= 1:
        return n
    dp = [0, 1]
    for i in range(2, n + 1):
        value = dp[i - 1] + dp[i - 2]
        dp.append(value)
    return dp[n]


def fib2(n):
    if n <= 1:
        return n
    a = 0
    b = 1
    for i in range(0, n - 1):
        c = a + b
        a = b
        b = c
    return c


n = int(input("enter the fibinocci u want to find : "))
# print(f"fibbinocci using memoization : {fib(n)}")
import datetime

start = datetime.datetime.now()
# print(f"fibbinocci using tabulation  : {fib1(n)}")
# print(f"fibbinocci using assign : {fib2(n)}")
print(f"fibbinocci using tabulation  : {fib2(n)}")
end = datetime.datetime.now()
print(f"time:{end-start}")
