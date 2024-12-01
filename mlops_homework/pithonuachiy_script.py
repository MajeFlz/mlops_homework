class InsufficientFundsError(Exception):
    def __init__(self, balance: float, amount: float) -> None:
        super().__init__(f"Недостаточно средств на счете! Баланс: {balance}, Сумма для списания: {amount}")
        self.balance = balance
        self.amount = amount


class BankAccount:
    def __init__(self, account_holder: str, initial_balance: float = 0.0) -> None:
        self.account_holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма депозита должна быть положительной.")
        self.balance += amount
        print(f"Счет {self.account_holder}: внесено {amount}. Текущий баланс: {self.balance}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Счет {self.account_holder}: снято {amount}. Текущий баланс: {self.balance}")

    def transfer(self, amount: float, recipient: 'BankAccount') -> None:
        print(f"Перевод {amount} со счета {self.account_holder} на счет {recipient.account_holder}")
        self.withdraw(amount)
        recipient.deposit(amount)

    def get_balance(self) -> float:
        return self.balance


def main() -> None:
    try:
        account1 = BankAccount("Иван", 1000.0)
        account2 = BankAccount("Анна", 500.0)

        account1.deposit(200.0)
        account2.withdraw(100.0)

        account1.transfer(300.0, account2)

        print(f"Баланс счета {account1.account_holder}: {account1.get_balance()}")
        print(f"Баланс счета {account2.account_holder}: {account2.get_balance()}")

    except InsufficientFundsError as e:
        print(f"Ошибка: {e}")
    except ValueError as e:
        print(f"Некорректная операция: {e}")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")


if __name__ == "__main__":
    main()
