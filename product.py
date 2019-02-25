def product(integers):
    total = 1
    for digit in integers:
        total *= digit
    return total


print(product([4, 5, 5]))


def productWhile(integers):
    total = 1
    length = len(integers)
    while length > 0:
        total *= integers[length - 1]
        length -= 1
    return total

print(productWhile([4, 5, 5, 6, 7]))
    

def countProductOfIntegers(integers):
    total = 1
    for digit in integers:
        total *= digit
    return total

print(countProductOfIntegers([4, 2, 3, 3, 2]))


def count_product_of_integers(integers):
    total = 1
    for x in integers:
        total *= x
    return total

print(count_product_of_integers([1, 2, 2, 1, 1, 2]))

def count_products(integers):
    length = len(integers)
    total = 1
    while length >= 1:
        total = total * integers[length - 1]
        length -= 1
    return total

print(count_products([1, 2, 4, 2, 3]))
        



