# Simple Bank System
class BankAccount:
	def __init__(self, owner, balance=0):
		self.owner = owner
		self.balance = balance

	def deposit(self, amount):
		if amount > 0:
			self.balance += amount
			print(f"Deposited ${amount}. New balance: ${self.balance}")
		else:
			print("Deposit amount must be positive.")

	def withdraw(self, amount):
		if amount > self.balance:
			print("Insufficient funds.")
		elif amount <= 0:
			print("Withdrawal amount must be positive.")
		else:
			self.balance -= amount
			print(f"Withdrew ${amount}. New balance: ${self.balance}")

	def check_balance(self):
		print(f"Current balance: ${self.balance}")


def main():
	print("Welcome to the Simple Bank System!")
	name = input("Enter your name to create an account: ")
	account = BankAccount(name)

	while True:
		print("\nChoose an option:")
		print("1. Deposit")
		print("2. Withdraw")
		print("3. Check Balance")
		print("4. Exit")
		choice = input("Enter your choice (1-4): ")

		if choice == '1':
			try:
				amount = float(input("Enter amount to deposit: "))
				account.deposit(amount)
			except ValueError:
				print("Invalid amount.")
		elif choice == '2':
			try:
				amount = float(input("Enter amount to withdraw: "))
				account.withdraw(amount)
			except ValueError:
				print("Invalid amount.")
		elif choice == '3':
			account.check_balance()
		elif choice == '4':
			print("Thank you for using the Simple Bank System. Goodbye!")
			break
		else:
			print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
	main()
