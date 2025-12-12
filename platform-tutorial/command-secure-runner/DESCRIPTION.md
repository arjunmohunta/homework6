# Bank Account Management System

## Overview
In this challenge, you will implement a console-based **Bank Account Management System** that simulates how a backend banking service manages customer accounts and financial transactions. The goal of this challenge is to practice **secure software engineering principles**, including input validation, state consistency, and defensive programming.

You are provided with starter code that contains the structure of the system and existing functionality. Several critical methods are intentionally left unimplemented. Your task is to complete these methods while ensuring the system behaves correctly and securely.

---

## Scenario
You are a junior software engineer working on the backend of a banking application. The system must ensure that all account operations are safe and consistent. Errors such as negative balances, duplicate accounts, or invalid transfers could represent serious security flaws in a real-world financial system.

Your task is to implement the missing logic so that the system enforces all constraints and passes the provided test cases.

---

## Account Model
Each bank account contains the following information:

- **Account Number**: A unique integer identifier
- **Account Holder Name**: A string
- **Balance**: A non-negative floating-point number
- **Account Type**: A string (e.g., Savings, Checking)

All account data is stored in memory for the duration of the program.

---

## Your Tasks
You must implement the logic for the following operations by modifying **only the TODO methods** in the starter code.

### 1. Add Account
- Account number must be unique
- Initial balance must be non-negative

### 2. Edit Account
- Update the account holder name
- Update the account type
- The account must already exist

### 3. Delete Account
- Permanently remove an account
- The account must already exist

### 4. Deposit Money
- Deposit amount must be positive
- The account must exist

### 5. Withdraw Money
- Withdrawal amount must be positive
- The account balance must not become negative
- The account must exist

### 6. Transfer Money
- Both source and destination accounts must exist
- Transfer amount must be positive
- The source account must have sufficient balance

### 7. Display Accounts
- Display all stored accounts and their details

---

## Constraints
- Do not use external libraries
- Store all accounts in memory
- Follow object-oriented design principles
- Modify only the TODO (empty) methods

---

## Security Focus
This challenge emphasizes secure coding practices, including:

- Input validation to prevent invalid or malicious values
- Preventing unauthorized or unsafe state changes
- Ensuring balance consistency across transactions
- Defensive programming to avoid runtime errors

Incorrect implementations may lead to vulnerabilities such as negative balances, inconsistent account state, or data loss.

---

## How to Complete the Challenge
1. Review the starter code and identify all TODO methods.
2. Implement the required logic while enforcing all constraints.
3. Run the provided test cases to verify your solution.
4. Ensure all tests pass without breaking existing functionality.

---

## Related Requirements
- **User Story:** US-02 – In-Browser Coding Challenges  
- **Use Case:** UC-05 – Submit Code for Evaluation  
- **Vision Goal:** VIS-01 – Teach real-world software security skills

---

## Expected Skills
- Object-oriented programming
- Lists and in-memory data structures
- Control flow and conditional logic
- Input validation and defensive coding
- Secure handling of stateful data
