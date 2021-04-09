def sum_recursion(n):
    if n > 1:
        return sum_recursion(n-1) + n
    else:
        return 0

sum = sum_recursion(500)
print(sum)