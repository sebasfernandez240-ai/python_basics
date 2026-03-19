def sum_or_product(number1, number2):
    if number1 * number2 <= 1000:
        return number1 * number2
    else:
        return number1 + number2
print(sum_or_product(20, 30))
print(sum_or_product(40, 30))
