# 1. Решить 6 задачу из семинара.
# Задание №6 Напишите программу банкомат.
# ✔Начальная сумма равна нулю
# ✔Допустимые действия: пополнить, снять, выйти
# ✔Сумма пополнения и снятия кратны 50 у.е.
# ✔Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔Нельзя снять больше, чем на счёте
# ✔При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной
# ✔Любое действие выводит сумму денег'''

class ATM:
    def __init__(self):
        self.balance = 0
        self.transactions = 0

    def deposit(self, amount):
        if amount % 50 != 0:
            print("Сумма пополнения должна быть кратна 50 у.е.")
            return
        if self.transactions % 3 == 0:
            print(f"Начислен процент: {self.balance * .03 :.2f} у.е.")
            self.balance += self.balance * .03
        self.balance += amount
        self.transactions += 1
        print(f"Вы пополнили счет на {amount :.2f} у.е. Баланс: {self.balance :.2f} у.е.")

    def withdraw(self, amount):
        if self.transactions % 3 == 0:
            self.balance += self.balance * .03
            print(f"Начислен процент: {self.balance * .03:.2f} у.е.")
        if amount % 50 != 0:
            print("Сумма снятия должна быть кратна 50 у.е.")
            return
        if self.balance <= 5_000_000:
            withdrawal_fee = min(max(amount * 0.015, 30), 600)
            amount -= withdrawal_fee
        if self.balance < amount:
            print("Недостаточно средств на счете.")
            return
        self.balance -= amount
        self.transactions += 1
        print(f"Вы сняли {amount :.2f} у.е. Баланс: {self.balance:.2f}")

    def exit(self):
        print(f"Баланс: {self.balance :.2f} у.е.")
        if self.balance > 5_000_000:
            wealth_tax = self.balance * .10
            print(f"Баланс на момент завершения: {self.balance - wealth_tax:.2f} у.е.")
            self.balance -= wealth_tax
            print(f"Удержан налог на богатство: {wealth_tax :.2f} у.е.")
        print("Сессия завершена. До свидания!")


def main():
    account = ATM()

    while True:
        print("\nВыберите действие:")
        print("1. Пополнить счет")
        print("2. Снять деньги")
        print("3. Выйти")
        choice = input("Введите номер действия: ")

        if choice == '1':
            amount = int(input("Введите сумму для пополнения: "))
            account.deposit(amount)
        elif choice == '2':
            amount = int(input("Введите сумму для снятия: "))
            account.withdraw(amount)
        elif choice == '3':
            account.exit()
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите действие снова.")


if __name__ == "__main__":
    main()


# 2. Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
# Функцию hex используйте для проверки своего результата.

def decimal_to_hexadecimal(decimal):
    hexadecimal_chars = "0123456789ABCDEF"
    if decimal == 0:
        return "0"
    result = ""
    while decimal > 0:
        remainder = decimal % 16
        result = hexadecimal_chars[remainder] + result
        decimal = decimal // 16
    return result


decimal_number = int(input("Введите целое число: "))


hexadecimal_representation = decimal_to_hexadecimal(decimal_number)

print(f"Шестнадцатеричное представление: {hexadecimal_representation}")
print(f"Шестнадцатеричное представление с Hex: {hex(decimal_number)}")

# 3. Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода
# используйте модуль fractions.


from fractions import Fraction

def parse_fraction(fraction_str):
    try:
        num, den = map(int, fraction_str.split('/'))
        return num, den
    except ValueError:
        return None

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def calculate_fraction_operations(fraction1, fraction2):
    parsed_fraction1 = parse_fraction(fraction1)
    parsed_fraction2 = parse_fraction(fraction2)

    if parsed_fraction1 is None or parsed_fraction2 is None:
        return None

    num1, den1 = parsed_fraction1
    num2, den2 = parsed_fraction2

    # Находим общий знаменатель
    common_denominator = den1 * den2 // gcd(den1, den2)

    # Вычисление суммы и произведения дробей
    sum_num = num1 * (common_denominator // den1) + num2 * (common_denominator // den2)
    product_num = num1 * num2

    return f"{sum_num}/{common_denominator}", f"{product_num}/{common_denominator}"

# Ввод дробей
fraction1: str = input("Введите первую дробь (в формате 'a/b'): ")
fraction2: str = input("Введите вторую дробь (в формате 'a/b'): ")


results = calculate_fraction_operations(fraction1, fraction2)



if results is not None:
    sum_result, product_result = results
    print(f"Сумма дробей: {sum_result}")
    print(f"Произведение дробей: {product_result}")
    print(f"Сумма дробей с функцией Fraction: {Fraction(sum_result)}")
    print(f"Произведение дробей с функцией Fraction: {Fraction(product_result)}")
else:
    print("Ошибка: Некорректный формат дробей.")
