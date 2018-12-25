def checkTheProductOfNumbers(integers):
    total = 1
    length = len(integers)
    digits = integers[:]
    while length > 0:
        total *= digits[length - 1]
        length -= 1
    return total

print(checkTheProductOfNumbers([4, 5, 5, 6, 7]))
    
