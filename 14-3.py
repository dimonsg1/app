choice = input("Выберите операцию: ")
number = int(input("Сколько операндов? "))
num1 = input("\nВведите первое число: ")
sum = int(num1)
pr = num1
	
for n in range(2, number + 1):
	print("\nВведите", n, end = "")
	num2 = input(" число: ")
	if choice == "+":
		sum += int(num2)
		pr += " + " + num2
	elif choice == "-":
		sum -= int(num2)
		pr += " - " + num2
	elif choice == "*":
		sum *= int(num2)
		pr += " * " + num2
	elif choice == "/":
		sum /= int(num2)
		pr += " / " + num2
	else:
		print("Ошибка: такой операции не существует. Попробуйте ещё раз.")

print(pr + " = ", sum)		