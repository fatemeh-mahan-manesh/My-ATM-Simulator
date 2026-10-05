import datetime

# مقدار اولیه‌ها
PIN = 1234
temp = 1
balance = 1000
transactions = []

# ورود PIN
password = int(input("Hi! Welcome to my ATM.\nPlease enter your PIN : "))

while password != PIN and temp < 3:
    temp += 1
    password = int(input(f"Wrong password. {3-temp} Attempt(s) left. Try again : "))

if password != PIN:
    print("Card blocked! Too many failed attempts.")

else:
    while True:
        page = int(input("""
1. Check Balance
2. Deposit
3. Withdraw
4. Exit
5. Transaction History
"""))

        if page == 1:
            print(f"Your balance is {balance}")

        elif page == 2:
            deposit = int(input("Please enter your desired amount to deposit : "))
            balance += deposit
            print(f"Your new balance is {balance}.")
            # ذخیره تراکنش با تاریخ و ساعت
            transactions.append(f"{datetime.datetime.now()} - Deposit: +{deposit}")

        elif page == 3:
            while True:
                withdraw = int(input("Please enter your desired amount to withdraw : "))
                if withdraw > balance:
                    print(f"Insufficient funds! Your current balance is {balance}. Try again.")
                else:
                    balance -= withdraw
                    print(f"Your new balance is {balance}.")
                    # ذخیره تراکنش با تاریخ و ساعت
                    transactions.append(f"{datetime.datetime.now()} - Withdraw: -{withdraw}")
                    break

        elif page == 4:
            print("Thank you for using my ATM. Goodbye!")
            break

        elif page == 5:
            if not transactions:
                print("No transactions yet.")
            else:
                print("Transaction History:")
                for t in transactions:
                    print(t)

        else:
            print("Invalid option! Please choose 1-5.")