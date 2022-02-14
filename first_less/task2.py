def sum_of_digits(value):
    result = 0

    while value != 0:
        result += value % 10
        value //= 10

    return result


arr = []
for i in range(1, 1001):
    if i % 2 == 1:
        arr.append(i ** 3)

sum1 = sum(filter(lambda numbers: sum_of_digits(numbers) % 7 == 0, arr))
sum2 = sum(filter(lambda numbers: sum_of_digits(numbers + 17) % 7 == 0, arr))


print(sum1)
print(sum2)

