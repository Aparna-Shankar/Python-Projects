'''
# Please create and implement a Calculator class, which makes use of the `addition` module.
# Your Calculator should achieve these goals:
# - It should implement `Addition.add()`, `subtract()`, `multiply()` and `divide()` methods.
# - It cannot use addition, subtraction, multiplication and division operators (`+`, `-`, `*` and `/`) directly.
#   Instead, it should be only based on the `Addition.add()` function from the `addition` module.
# - To simplify the problem, you may expect input for the multiply() and divide() methods are all non-integers,
#   and will always be valid, i.e. all non-negative integers and no 0 as divisor.
'''

from addition import Addition


class Calculator:
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)

    @classmethod
    def subtract(cls, num1, num2):
        return Addition.add(num1, -num2)

    @classmethod
    def multiply(cls, num1, num2):
        prod = 0
        for i in range(num1):
            prod = Addition.add(prod, num2)
        return prod

    @classmethod
    def divide(cls, num1, num2):
        result = 0
        rem = num1
        while rem >= num2:
            rem = Addition.add(rem, -num2)
            result = Addition.add( result, 1 )
            if rem < num2:
                break
        return result

print(Calculator.divide(24,6))

