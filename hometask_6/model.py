"""
Допущения:
- для хранения баланса на счете подходит int
- все бизнес-проверки основаны только на неотрицательности текущего баланса и суммы операции
- отмена операции сама по себе не является операцией
"""


class Account:
    pass


class AccountOperation:
    def __init__(self, account: Account, value: int):
        if value <= 0:
            raise Exception(f"Некорректное значение суммы операции(отрицательная): {value}")
        self.account = account
        self.value = value

    def do(self):
        pass

    def undo(self):
        pass


class Account:
    def __init__(self, name: str, started_balance: int):
        if started_balance < 0:
            raise Exception(f"Некорректное значение баланса(отрицательное): {started_balance} для счета {name}")
        self.name = name
        self.balance = started_balance
        self.history = []

    def up(self, value: int):
        self.__do_operation(UpAccountOperation(self, value))

    def withdraw(self, value: int):
        self.__do_operation(WithdrawAccountOperation(self, value))

    def cancel_last_operation(self):
        if not self.history:
            raise Exception(f"У счета {self.name} отсутствуют выполненные операции")
        operation = self.history.pop()
        operation.undo()

    def __do_operation(self, operation: AccountOperation):
        operation.do()
        self.history.append(operation)


class UpAccountOperation(AccountOperation):

    def do(self):
        new_value = self.account.balance + self.value
        self.account.balance = new_value

    def undo(self):
        new_value = self.account.balance - self.value
        self.account.balance = new_value


class WithdrawAccountOperation(AccountOperation):

    def __init__(self, account: Account, value: int):
        if account.balance - value < 0:
            raise Exception(f"Недостаточно средств для проведения операции по счету {account.name}")
        super().__init__(account, value)

    def do(self):
        new_value = self.account.balance - self.value
        self.account.balance = new_value

    def undo(self):
        new_value = self.account.balance + self.value
        self.account.balance = new_value
