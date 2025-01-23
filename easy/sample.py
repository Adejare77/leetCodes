#!/usr/bin/env python3


# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1

#     return fibonacci(n-1) + fibonacci(n-2)

# def fibonacci(n):
#     if n == 0:
#         return [0]
#     elif n == 1:
#         return [0, 1]

#     prev = fibonacci(n - 1)
#     return prev + [prev[-1] + prev[-2]]

# # Example Usage
# n = 9
# print(fibonacci(n))

x = "a"
y = "A"

if ord(x) + 32 == ord(y) and ord(x) - 32 != ord(y):
    print("YESS")
print(ord("a"))
