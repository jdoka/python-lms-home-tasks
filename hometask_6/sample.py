from hometask_6.model import Account

started_balance = 1000
up_sum = 300
withdraw_sum = 500
incorrect_value = -100
account = Account("Счет1", started_balance)

# happy path
print(account.balance == started_balance)

account.up(up_sum)
print(account.balance == started_balance + up_sum)

account.withdraw(withdraw_sum)
print(account.balance == started_balance + up_sum - withdraw_sum)

account.cancel_last_operation()
print(account.balance == started_balance + up_sum)

account.cancel_last_operation()
print(account.balance == started_balance)

# fail
try:
    account.up(incorrect_value)
except Exception as e:
    print(e.args[0] == f"Некорректное значение суммы операции(не положительная): {incorrect_value}")
try:
    account.withdraw(5000)
except Exception as e1:
    print(e1.args[0] == f"Недостаточно средств для проведения операции по счету {account.name}")
try:
    account.cancel_last_operation()
except Exception as e2:
    print(e2.args[0] == f"У счета {account.name} отсутствуют выполненные операции")
try:
    account_name = "Некорректный счет"
    Account(account_name, incorrect_value)
except Exception as e3:
    print(e3.args[0] == f"Некорректное значение баланса(отрицательное): {incorrect_value} для счета {account_name}")
