def fibonacciNumbersBelow(number):
    numbers = [1]

    num = 2

    while num < number:
        numbers.append(num)
        lastTwo = numbers[-2:]
        num = lastTwo[0] + lastTwo[1]


    return numbers
