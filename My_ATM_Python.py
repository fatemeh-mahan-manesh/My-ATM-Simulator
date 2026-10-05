PIN = 1234
temp = 1
balance = 1000
page = 0
password = int(input("""Hi! Welcome to my ATM.
Please enter your PIN : """))

while password != PIN and temp < 3 :
	password = int(input(f"""Wrong password.
	{3-temp} Attempt(s) left.
	Try again : """))
	temp += 1
if password != PIN:
	print("Card blocked! Too many failed attempts.")
	
else :
	while password == PIN :
		page = int(input("""
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
"""))

		if page == 1 :
			print(f"Your balance is {balance}")
			page = int(input("To exit press 4 : "))

		elif page == 2 :
			deposit = int(input("Please enter your desired amount to deposit : "))
			balance += deposit
			print(f"Youre new balance is {balance}.")
			page = int(input("To exit press 4 : "))
	
		elif page == 3 :
			while True :
				withdraw = int(input("Please enter your desired amount to withdraw : "))
				if withdraw > balance :
					print("Your desired amount is more than your balance.")
				else :
					balance -= withdraw
					print(f"Your new balance is {balance}.")
					break
			page = int(input("To exit press 4 : "))
		elif page == 4 :
			print("Thank you for using my ATM.")
			break
		else:
			page =int(input("Invalid option! Please choose 1-4 : "))