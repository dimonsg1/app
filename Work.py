def sum_factorials(num):
    part_factorials = 1
    summa = 0

    for i in range(1, num + 1):
        part_factorials *= i
        summa += part_factorials
    return summa

n = int(input("Введите число: "))
print(sum_factorials(n))
