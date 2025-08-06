"""
3. Clase CuentaBancaria con encapsulamiento (Nivel Intermedio)
🧩 Objetivo:1
Encapsular atributos

Usar getters y setters

Validar datos

📋 Enunciado:
Crea una clase CuentaBancaria con los atributos privados titular y saldo.
Agrega métodos para depositar() y retirar() dinero (verificando que haya saldo suficiente).
Crea un método mostrar_saldo()

🧪 Extra:
Evita que el saldo pueda ser negativo. Lanza errores personalizados si es necesario.

"""
#Import bankAccount class
from bankAccount import BankAccount

#Creare accounts
accounts = [
    BankAccount("Victor Muntane", 1260),
    BankAccount("Mar Zaragoza", 350)
]

text = ""
while text != "exit":

    print("\n------ BANK ACCOUNTS ------")
    for index, account in enumerate(accounts):
        print(f"{index+1}. {account.getHolder()}")

    print("0. Exit")

    try:
        bnkA = int(input("\nSelect number Account: "))
        if(bnkA != 0):
            txt = ""
            while txt != "exit":
                try:
                    print(f"\n------ {accounts[bnkA-1].getHolder().upper()} ACCOUNT ------")
                    print("1. Deposit")
                    print("2. Withdraw")
                    print("3. Balance")
                    print("0. Exit")
                    opertation = int(input("\nSelect one option: "))
                    if opertation == 1:
                        amount = int(input("Select the amount to deposit: "))
                        print(accounts[bnkA-1].deposit(amount))
                    elif opertation == 2:
                        amount = int(input("Select the amount to withdraw: "))
                        print(accounts[bnkA-1].withdraw(amount))
                    elif opertation == 3:
                        print(accounts[bnkA-1].showBalance())
                    elif opertation == 0:
                        print("\nGOODBYE!")
                        txt = "exit"
                    else:
                        print("\nEnter a valid value!")
                except ValueError:
                   print("\nEnter a valid value value!") 
            
        else:
            print("\nGOODBYE!")
            text = "exit"
    except (ValueError, IndexError):
        print("\nEnter a valid value!")
    


