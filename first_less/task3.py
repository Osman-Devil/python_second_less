word = "Процент"

for numbers in range(1, 101):
    if 4 < numbers < 20:
        print(str(numbers) + " " + word + 'ов')
    elif numbers % 10 == 2 or numbers % 10 == 3 or numbers % 10 == 4:
        print(str(numbers) + " " + word + 'a')
    elif numbers % 10 == 1:
        print(str(numbers) + " " + word)
    else:
        print(str(numbers) + " " + word + 'ов')
