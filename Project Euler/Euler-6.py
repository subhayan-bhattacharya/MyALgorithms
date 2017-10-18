n = 100
square_sum = 0
for i in range(1,n+1):
    square = i ** 2
    square_sum = square_sum + square

sum_square = n * (n + 1)
sum_square = sum_square // 2
sum_square = sum_square ** 2
print (abs(sum_square - square_sum))
