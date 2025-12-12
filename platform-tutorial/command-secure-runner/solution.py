class BankAccount:
    def __init__(self,acc_no,name,balance,acc_type):
        self.acc_no=acc_no
        self.name=name
        self.balance=balance
        self.acc_type=acc_type
    def update_name(self,new_name):
        self.name=new_name
    def update_type(self,new_type):
        self.acc_type=new_type
    def credit(self,amount):
        self.balance+=amount
    def debit(self,amount):
        self.balance-=amount

class Bank:
    def __init__(self):
        self.accounts=[]
    def find_account(self,acc_no):
        for acc in self.accounts:
            if acc.acc_no==acc_no:
                return acc
        return None
    def add_account(self,acc_no,name,balance,acc_type):
        if self.find_account(acc_no) is None:
            self.accounts.append(BankAccount(acc_no,name,balance,acc_type))
    def edit_account(self,acc_no,new_name,new_type):
        acc=self.find_account(acc_no)
        if acc:
            acc.update_name(new_name)
            acc.update_type(new_type)
    def delete_account(self,acc_no):
        acc=self.find_account(acc_no)
        if acc:
            self.accounts.remove(acc)
    def deposit(self,acc_no,amount):
        acc=self.find_account(acc_no)
        if acc:
            acc.credit(amount)
    def withdraw(self,acc_no,amount):
        acc=self.find_account(acc_no)
        if acc:
            acc.debit(amount)
    def transfer(self,from_acc,to_acc,amount):
        src=self.find_account(from_acc)
        dst=self.find_account(to_acc)
        if src and dst:
            src.debit(amount)
            dst.credit(amount)
    def get_all_accounts(self):
        return self.accounts
    def account_exists(self,acc_no):
        return self.find_account(acc_no) is not None

class InputHandler:
    def read_int(self):
        return int(input())
    def read_float(self):
        return float(input())
    def read_string(self):
        return input()

class BankUI:
    def __init__(self,bank):
        self.bank=bank
        self.input=InputHandler()
    def print_menu(self):
        print("1 Create Account")
        print("2 Edit Account")
        print("3 Delete Account")
        print("4 Deposit")
        print("5 Withdraw")
        print("6 Transfer")
        print("7 Display One Account")
        print("8 Display All Accounts")
        print("9 Exit")
    def create_account(self):
        acc_no=self.input.read_int()
        name=self.input.read_string()
        balance=self.input.read_float()
        acc_type=self.input.read_string()
        self.bank.add_account(acc_no,name,balance,acc_type)
    def edit_account(self):
        acc_no=self.input.read_int()
        name=self.input.read_string()
        acc_type=self.input.read_string()
        self.bank.edit_account(acc_no,name,acc_type)
    def delete_account(self):
        acc_no=self.input.read_int()
        self.bank.delete_account(acc_no)
    def deposit(self):
        acc_no=self.input.read_int()
        amount=self.input.read_float()
        self.bank.deposit(acc_no,amount)
    def withdraw(self):
        acc_no=self.input.read_int()
        amount=self.input.read_float()
        self.bank.withdraw(acc_no,amount)
    def transfer(self):
        from_acc=self.input.read_int()
        to_acc=self.input.read_int()
        amount=self.input.read_float()
        self.bank.transfer(from_acc,to_acc,amount)
    def display_one(self):
        acc_no=self.input.read_int()
        acc=self.bank.find_account(acc_no)
        if acc:
            print(acc.acc_no,acc.name,acc.balance,acc.acc_type)
        else:
            print("Account not found")
    def display_all(self):
        accounts=self.bank.get_all_accounts()
        if not accounts:
            print("No accounts")
        for acc in accounts:
            print(acc.acc_no,acc.name,acc.balance,acc.acc_type)
    def run(self):
        while True:
            self.print_menu()
            choice=input()
            if choice=="1":
                self.create_account()
            elif choice=="2":
                self.edit_account()
            elif choice=="3":
                self.delete_account()
            elif choice=="4":
                self.deposit()
            elif choice=="5":
                self.withdraw()
            elif choice=="6":
                self.transfer()
            elif choice=="7":
                self.display_one()
            elif choice=="8":
                self.display_all()
            elif choice=="9":
                break
            else:
                print("Invalid choice")

def main():
    bank=Bank()
    ui=BankUI(bank)
    ui.run()

main()
