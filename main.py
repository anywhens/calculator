import math

memory = 0.0

def print_menu():
    print("""
Выберите операцию:
1. Сложение (+)
2. Вычитание (-)
3. Умножение (*)
4. Деление (/)
5. Возведение в степень (^)
6. Корень n-й степени (root)
7. Логарифм (log)
8. Синус (sin)
9. Косинус (cos)
10. Тангенс (tan)
11. Память: сохранить текущее число в память (mem_store)
12. Память: загрузить число из памяти (mem_load)
13. Очистить память (mem_clear)
14. Выйти (exit)
""")

def get_number(prompt="Введите число: "):
    while True:
        try:
            val = input(prompt)
            if val.lower() == 'm':
                return memory
            return float(val)
        except ValueError:
            print("Ошибка ввода. Попробуйте еще раз или введите 'm' для использования числа из памяти.")

def main():
    global memory
    current = 0.0
    print("Добро пожаловать в расширенный консольный калькулятор!")
    print("Для использования числа из памяти введите 'm' вместо числа.")
    while True:
        print(f"\nТекущее значение: {current}")
        print_menu()
        choice = input("Введите номер операции: ").strip()

        if choice == '1':
            x = get_number()
            y = get_number()
            current = x + y
        elif choice == '2':
            x = get_number()
            y = get_number()
            current = x - y
        elif choice == '3':
            x = get_number()
            y = get_number()
            current = x * y
        elif choice == '4':
            x = get_number()
            y = get_number()
            if y == 0:
                print("Ошибка: деление на ноль!")
                continue
            current = x / y
        elif choice == '5':
            x = get_number()
            y = get_number()
            current = x ** y
        elif choice == '6':
            n = get_number("Введите степень корня n: ")
            x = get_number("Введите число: ")
            if n == 0:
                print("Ошибка: степень корня не может быть нулём.")
                continue
            if x < 0 and n % 2 == 0:
                print("Ошибка: корень чётной степени из отрицательного числа не определён в действительных числах.")
                continue
            current = x ** (1 / n)
        elif choice == '7':
            base = get_number("Введите основание логарифма: ")
            x = get_number("Введите число: ")
            if base <= 0 or base == 1 or x <= 0:
                print("Ошибка: основание логарифма должно быть > 0 и != 1, число > 0.")
                continue
            current = math.log(x, base)
        elif choice == '8':
            angle = get_number("Введите угол в градусах: ")
            current = math.sin(math.radians(angle))
        elif choice == '9':
            angle = get_number("Введите угол в градусах: ")
            current = math.cos(math.radians(angle))
        elif choice == '10':
            angle = get_number("Введите угол в градусах: ")
            current = math.tan(math.radians(angle))
        elif choice == '11':
            memory = current
            print(f"Число {current} сохранено в памяти.")
        elif choice == '12':
            current = memory
            print(f"Загружено число из памяти: {memory}")
        elif choice == '13':
            memory = 0.0
            print("Память очищена.")
        elif choice == '14' or choice.lower() == 'exit':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор операции. Попробуйте снова.")
            continue

if __name__ == "__main__":
    main()
