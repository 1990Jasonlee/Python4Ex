def factorial():
    number = int(input('Enter number between 0 - 994:'))
    num = 1
    if number >= 1:
        for i in range(1, number + 1):
            num = num * i
    print(num)


factorial()
