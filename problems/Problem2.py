# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

from modules.Fibonacci import fibonacciNumbersBelow


def solve():
    sequence = fibonacciNumbersBelow(4000000)
    problem_sum = 0
    for number in sequence:
        if number % 2 == 0:
            problem_sum += number

    return problem_sum


solution = solve()
print(solution)
