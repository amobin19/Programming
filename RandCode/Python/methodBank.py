class BankAccount(object):
	def __init__(self, initial_balance=0):
		self.balance = initial_balance
	def deposit(self, amount):
		self.balance += amount
	def withdraw(self, amount):
		self.balance -= amount
	def overdrawn(self):
		return self.balance < 0
money = int(input("Initial amount: "))
my_account = BankAccount(money)
while(True):
	if(my_account.overdrawn == False):
		my_account.withdraw(5)
		my_account.withdraw(11)
	else:
		print("overdrawn")
		break
