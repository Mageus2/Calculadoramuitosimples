def main():
    while True:
        print("Escolha qual operação deseja realizar:")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Potenciação")
        escolha=input("Digite o número da operação: ")
        if escolha.isdigit() and int(escolha) in [1,2,3,4,5]:
            num1=float(input("Digite o primeiro número: "))
            num2=float(input("Digite o segundo número: "))
            if calculo(int(escolha), num1, num2)!=None:
                print("O resultado é:" , calculo(int(escolha), num1, num2))
                cont=input("Continuar? (s/n): ")
                cont=cont.lower()
                if cont!=("s"):
                    print("Ok!")
                    break
            else:
                cont=input("Continuar? (s/n): ")
                cont=cont.lower()
                if cont!=("s"):
                    print("Ok!")
                    break
                    
        else:
            print("Por favor digite um número válido.")
            cont=input("Continuar? (s/n): ")
            cont=cont.lower()
            if cont!=("s"):
                print("Ok!")
                break
            
                
def calculo(operacao, x , y):
    
    if operacao==1:
        return(round(x+y,2))
    elif operacao==2:
        return(round(x-y,2))
    elif operacao==3:
        return(round(x*y,2))
    elif operacao==4:
        if y==0:
            print("Não é possível dividir por 0")
            return None
        else:
            return(round(x/y,2))
    elif operacao==5:
        return(round(x**y,2))
               
print("Bem vindo a calculadora!")
main()
        
                
        
    