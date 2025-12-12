from bank import Bank,BankAccount

def run_tests():
    bank=Bank()
    try:
        bank.add_account(1,"Alice",1000,"Savings")
        bank.add_account(2,"Bob",500,"Current")
        bank.deposit(1,500)
        bank.withdraw(2,200)
        bank.transfer(1,2,300)
        acc1=bank.find_account(1)
        acc2=bank.find_account(2)
        assert acc1.balance==1200
        assert acc2.balance==600
        bank.edit_account(1,"Alice Smith","Savings")
        bank.delete_account(2)
        assert bank.find_account(2) is None
        print("All tests passed")
    except Exception as e:
        print("Test failed:",e)

if __name__=="__main__":
    run_tests()
