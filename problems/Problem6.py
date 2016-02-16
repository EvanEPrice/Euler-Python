#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_of_squares = 0
problem_range = range(1, 101)

for i in problem_range:
    sum_of_squares += i*i

print(sum_of_squares)

sum_of_range = sum(problem_range)

square_of_sum = sum_of_range*sum_of_range

difference = square_of_sum - sum_of_squares

print(difference)
