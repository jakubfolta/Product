def product(integers):
    total = 1
    for digit in integers:
        total *= digit
    return total


print(product([4, 5, 5]))


def productWhile(integers):
    total = 1
    length = len(integers)
    digits = integers[:]
    while length > 0:
        total *= digits[length - 1]
        length -= 1
    return total

print(productWhile([4, 5, 5, 6, 7]))
    
