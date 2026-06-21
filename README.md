# 🏦 Python OOP Banking System

A simple console-based banking system built using Python Object-Oriented Programming (OOP) concepts such as **Abstraction, Inheritance, Encapsulation, and Polymorphism**.

This project simulates basic banking operations like deposit, withdrawal, and balance checking for different types of accounts.

---

## 🚀 Features

- 🔐 Abstract base class for account structure (`Account`)
- 💰 Deposit system with validation
- 🏧 Withdrawal system with rules:
  - Savings Account: Cannot withdraw more than balance
  - Current Account: Allows overdraft up to 500
- 📊 Balance inquiry feature
- 🧠 Input validation for safe transactions
- 🖥️ Interactive CLI menu system

---

## 🏗️ OOP Concepts Used

- **Abstraction** → Using `ABC` and `@abstractmethod`
- **Inheritance** → `SavingAccount` and `CurrentAccount` inherit from `Account`
- **Encapsulation** → `_balance` is protected, controlled via methods
- **Polymorphism** → Different `withdraw()` behavior in each account type

---

## 📂 Project Structure


.
├── banking.py # Main program file
└── README.md


---

## ▶️ How to Run

### 1. Clone the repository
```bash
git clone https://github.com/your-username/python-oop-banking-system.git
cd python-oop-banking-system
2. Run the program
python banking.py
🧾 Menu Options

When you run the program, you will see:

1. Show Balance
2. Deposit
3. Withdraw
4. Exit
Account Types:
1 → Saving Account
2 → Current Account
💡 Example Usage
Deposit
Enter amount = 1000
Deposit Successful!
Withdraw
Enter amount = 500
Withdraw Successful!
Balance
Current Balance: 1500
⚠️ Rules
Amount must be a positive number
Invalid inputs will be rejected
Savings account cannot go below zero balance
Current account allows overdraft up to -500
📌 Future Improvements
Add interest calculation for savings account
Add transaction history
Add PIN/security system
Store data in file or database
GUI version using Tkinter or PyQt
👨‍💻 Author
Built by: Jahid
Purpose: Learning Python OOP and real-world system design
📜 License

This project is open-source and available for learning purposes.
