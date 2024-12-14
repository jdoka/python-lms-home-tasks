from hometask_6.model import Account

started_balance = 1000
up_sum = 300
withdraw_sum = 500
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
    account.up(-100)
except Exception as e:
    print(e.args[0])
try:
    account.withdraw(5000)
except Exception as e1:
    print(e1.args[0])
try:
    account.cancel_last_operation()
except Exception as e2:
    print(e2.args[0])
try:
    Account("Некорректный счет", -1000)
except Exception as e3:
    print(e3.args[0])
