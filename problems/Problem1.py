#Find the sum of all the multiples of 3 or 5 below 1000.


def solve():
    problem_sum = 0
    for num in range(1,1000):
        if num % 3 == 0 or num % 5 == 0:
            problem_sum += num
    return problem_sum

solution = solve()
print(solution)

