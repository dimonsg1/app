while True:
  num1 = int(input("\nВведите первое число: "))
  num2 = int(input("Введите второе число: "))
  
  choice = input("Выберите операцию: ")
  if choice == "+":
    print(num1, "+", num2, "=", num1 + num2)
  elif choice == "-":
    print(num1, "-", num2, "=", num1 - num2)
  elif choice == "*":
    print(num1, "*", num2, "=", num1 * num2)
  elif choice == "/":
    print(num1, "/", num2, "=", num1 * num2)
  else:
    print("Ошибка: такой операции не существует. Попробуйте ещё раз.")