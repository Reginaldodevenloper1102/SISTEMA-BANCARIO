menu= """
[d]Depositar
[s]Sacar
[e]Extrato
[q]Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    
    opcao = input(menu)
    
    if opcao =="d":
        valor = float(input("Informe o valor do deposito: "))
        
        if valor>0:
            saldo += valor
            extrato += f"depósito: R$ {valor:.2f}\n"
            
        else:
            print("Operação fahou o valor informado é invalido") 
            
            
    elif opcao == "s":
        valor = float(input("Informe o valor de saque "))
        
        excedeu_saldo = valor > saldo
        
        excedeu_limite = valor > limite
        
        excedeu_saque = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Operação falhou: Você não tem saldo suficiente.")
        
        elif excedeu_limite:
            print("Operação falhou: o valor de saque excede o limite. ")
            
        elif excedeu_saque:
            print("Operação falhou: número máximo de saque excedido.")
            
        elif valor > 0:
            saldo -= valor
            extrato += f"saque: R$ {valor:.2f}\n"
            numero_saques += 1
            
            
    elif opcao == "e":
        print("\n==============EXTRATO=============")
        print("não foram realizados movimentações." if not extrato else extrato)
        print(f"\nsaldo: R$ {saldo:.2f}")
        print("=======================")        
            
    elif opcao == "q":
        break
        
    else:
        print("Operação Inválida, por favor selecione novamente a operação desejada ")        
                        
        
                 