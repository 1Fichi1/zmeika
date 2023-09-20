import math
def main():
    while True:
        print("Выберите операцию:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Квадратный корень")
        print("7. Факториал")
        print("8. Синус")
        print("9. Косинус")
        print("10. Тангенс")
        print("0. Выход")

        plack = input("Введите номер операции: ")

        if plack == '0':
            break
        elif plack in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            try:
                num1 = float(input("Введите первое число: "))
                if plack != '6' and plack != '7' and plack != '8' and plack != '9':
                    num2 = float(input("Введите второе число: "))
            except ValueError:
                print("Ошибка: Введите корректное число.")
                continue

            if plack == '1':
                result = num1 + num2
            elif plack == '2':
                result = num1 - num2
            elif plack == '3':
                result = num1 * num2
            elif plack == '4':
                if num2 == 0:
                    print("Ошибка: Деление на ноль.")
                    continue
                result = num1 / num2
            elif plack == '5':
                result = num1 ** num2
            elif plack == '6':
                if num1 < 0:
                    print("Ошибка: Квадратный корень отрицательного числа.")
                    continue
                result = math.sqrt(num1)
            elif plack == '7':
                if num1 < 0:
                    print("Ошибка: Факториал отрицательного числа.")
                    continue
                result = math.factorial(int(num1))
            elif plack == '8':
                result = math.sin(num1)
            elif plack == '9':
                result = math.cos(num1)
            elif plack == '10':
                result = math.tan(num1)

            print(f"Результат: {result}")
        else:
            print("Ошибка: Введите корректный номер операции.")


if __name__ == "__main__":
    main()