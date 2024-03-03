print('Calculadora')
opciones = 0
import math

while opciones != 6:

    print("1-.Suma")
    print("2-.Resta")
    print("3-.Multiplicaicon")
    print("4-.Divicion")
    print("5-.Raiz Cuadrada")
    print("6-.Salir")

    opciones = int(input("Ingrese una opcion: "))

    if opciones == 1:
        numb_1=0
        numb_2=0
        numb_1= int (input("Ingrese un numero: ")) 
        numb_2 = int (input("Ingrese un numero: "))
        print('\n\t\tResultado=',numb_1 + numb_2) 

    if opciones == 2:
        numb_1=0
        numb_2=0
        numb_1= int (input("Ingrese un numero: ")) 
        numb_2 = int (input("Ingrese un numero: "))
        print('\n\t\tResultado=',numb_1 - numb_2) 
    
    if opciones == 3:
        numb_1=0
        numb_2=0
        numb_1= int (input("Ingrese un numero: ")) 
        numb_2 = int (input("Ingrese un numero: "))
        print('\n\t\tResultado=',numb_1 * numb_2) 
    
    if opciones == 4:
        numb_1=0
        numb_2=0
        numb_1= int (input("Ingrese un numero: ")) 
        numb_2 = int (input("Ingrese un numero: "))
        print('\n\t\tResultado=',numb_1 / numb_2) 
    
    if opciones == 5:
        numb_1=0
        numb_2=0
        numb_1= int (input("Ingrese un numero: ")) 
        numb_2 = int (input("Ingrese un numero: "))
        print(f'\t\tResultado de su numero {numb_1}= {math.sqrt(numb_1):.2f}') 
        print(f'\t\tResultado de su numero {numb_2}= {math.sqrt(numb_2):.2f}') 
   
    if opciones == 6:
        print("\n\t\t\tPrograma Finalizado")
        
    

       
   