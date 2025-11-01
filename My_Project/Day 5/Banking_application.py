balance = 0.0
kyc_documents = {}
def check_balance(balance):
    print(f"Your current balance is : {balance}")
    print("=============================================================")


def deposite(amt):
    global balance
    if amt>0:
        balance=balance+amt
        print("Amount deposited successfully")
        print(f"\nYour current balance is : {balance}")
        print("=============================================================")
    else:
        print("Cannot deposit -ve or zero amount")
        print("=============================================================")

def withdraw(amt):
    global balance
    if amt<=0:
        print("Cannot withdraw less than 0")
        print("=============================================================")
    elif amt>balance:
        print(f"Your current balance is : {balance}\n you can withdraw {amt} from account")
        print("=============================================================")
    else:
        balance=balance-amt
        print("Amount withdrawn successfully!")
        print(f"\nYour current balance is : {balance}")
        print("=============================================================")
def update_kyc_documents(docs):
    global kyc_documents
    kyc_documents.update(docs)

def check_kyc_documents():
    if len(kyc_documents)==0:
        print("KYC IS NOT DONE!\nPLEASE UPDATE THE KYC DOCUMENTS")
        print("=============================================================")
    else:
        print("=============================================================")
        for doc in kyc_documents:
            print(f"{doc} : {kyc_documents[doc]}") # to get key value pair from dict doc: is key and kyc_document[doc] will return value
        print("YOUR KYC IS UPDATED!")
        print("=============================================================")

if __name__=='__main__':
    print("=============================================================")
    print("Welcome to Banking Application")
    print("=============================================================")
    while True:
        print("1.Check balance")
        print("2.Deposit an Amount")
        print("3.Withdraw an Amount")
        print("4.Check Kyc Documents")
        print("5.Update Kyc Documents")
        print("6.Exit")
        print("=============================================================")

        choice=input("Enter your choice (1-6): ")
        print("=============================================================")
        if choice=='1':
            check_balance(balance)
        elif choice=='2':
            amt = float(input("Enter your amount to deposit: "))
            deposite(amt)

        elif choice=='3':
            amt= float(input("Enter your amount to withdraw: "))
            withdraw(amt)
        elif choice=='4':
            check_kyc_documents()
        elif choice=='5':
            docs={}
            n_documents = input("Enter number of documents you want to add:")
            for i in range(int(n_documents)):
                key=input("Enter  of document type:")
                val = input("Enter Document Number:")
                docs[key]=val
            update_kyc_documents(docs)
            print("Documents updated successfully and KYC is done")
            print("\n=============================================================")
        elif choice=='6':
            break
        else:
            print("Invalid choice!! Please retry")
            print("=============================================================")

    print("\nThank You For Banking with Us")