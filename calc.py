def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def main():
    print("Мини-калькулятор")
    print("1. Сложение")
    print("2. Вычитание")
    print("3. Умножение")
    print("4. Деление")
    print("0. Выход")
    while True:
        choice = input("Выберите операцию: ")
        if choice == "0":
            print("До свидания!")
            break
        if choice not in ("1", "2", "3", "4"):
            print("Неверный выбор")
            continue
        a = float(input("Введите первое число: "))
        b = float(input("Введите второе число: "))
        if choice == "1":
            print("Результат:", add(a, b))
        elif choice == "2":
            print("Результат:", subtract(a, b))
        elif choice == "3":
            print("Результат:", multiply(a, b))
        elif choice == "4":
            print("Результат:", divide(a, b))

if __name__ == "__main__":
    main()