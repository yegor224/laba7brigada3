import math

def calculator():
    print("Простой калькулятор на Python")
    print("Доступные операции: +, -, *, /, ln, sin, cos, exit")

    while True:
        operation = input("\nВведите операцию: ").strip().lower()

        if operation == "exit":
            print("Выход из калькулятора.")
            break

        if operation in ["+", "-", "*", "/"]:
            try:
                a = float(input("Введите первое число: "))
                b = float(input("Введите второе число: "))

                if operation == "+":
                    result = a + b
                elif operation == "-":
                    result = a - b
                elif operation == "*":
                    result = a * b
                elif operation == "/":
                    if b == 0:
                        print("Ошибка: деление на ноль.")
                        continue
                    result = a / b

                print(f"Результат: {result}")
            except ValueError:
                print("Ошибка: введите корректные числа.")

        elif operation in ["ln", "sin", "cos"]:
            try:
                x = float(input("Введите значение x: "))

                if operation == "ln":
                    if x <= 0:
                        print("Ошибка: логарифм определён только для положительных чисел.")
                        continue
                    result = math.log(x)
                elif operation == "sin":
                    result = math.sin(x)
                elif operation == "cos":
                    result = math.cos(x)

                print(f"Результат: {result}")
            except ValueError:
                print("Ошибка: введите корректное число.")
        else:
            print("Неизвестная операция. Попробуйте ещё раз.")

if __name__ == "__main__":
    calculator()
