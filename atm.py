class Atm(object):
    def __init__(self,user,atm_card_number,pin_number):
       self.user=user
       self.atm_card_number:atm_card_number
       self.pin_number:pin_number
       self.balance=0

    def choice(self):
        print("Choose one of the following to proceed")
        choice=int(input("1 to Check Balance \t 2 to Deposit Money \t 3 to Withdraw Money \t 4 to Exit \n =>"))
        if(choice==1):
            self.BalanceInquiry()
        elif(choice==2):
            self.CashDeposit()
        elif(choice==3):
            self.CashWithdrawl()
        elif(choice==4):
            print("Thank you!")
        else:
            print("Invalid input, try again")
            self.choice()
        
    def CashWithdrawl(self):
        amount =input("Enter the amount you wish to withdraw: ")
        self.balance-=int(amount)
        with open("balancesheet.txt","a") as file:
            file.write(str(self.balance)+" \n")
        print("Current Amount is: "+str(self.balance))
        self.choice()


    def BalanceInquiry(self):
        print("Your balance is :"+str(self.balance))
        self.choice()

    
    def CashDeposit(self):
        amount=input("Enter the amount you wish to submit: ")
        self.balance+=int(amount)
        with open("balancesheet.txt","a") as file:
            file.write(str(self.balance)+" \n")
        print("Current Amount is: "+str(self.balance))
        self.choice()


    def AccessBalanceSheet(self):
        with open("balancesheet.txt","r") as file:
            for amount in file:
                pass
            self.balance=int(amount)

name=input("Enter your name: \n")
card_number=input("Enter card number: \n")
pin=input("Enter your pin: \n")
user1=Atm(name, card_number,pin)
user1.AccessBalanceSheet()
user1.choice()
