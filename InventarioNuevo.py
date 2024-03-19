import os

existencias_arroz = 0
existencias_queso = 0
existencias_frijoles = 0

def fnt_limpiarPantalla():
    os.system('cls')
    print('Autor: Michell Mosquera P. -2024')
    print('Versión : V1.0')
    
    fnt_existencias()
def fnt_existencias():
    global existencias_arroz
    global existencias_queso
    global existencias_frijoles
    print('\n----EXISTENCIAS ACTUALES----')
    print(f'\nArroz X bulto 250 kg............ {existencias_arroz}')
    print(f'\nQueso X bloque 10 kg............ {existencias_queso}')
    print(f'\nFrijol X bulto 150 kg........... {existencias_frijoles}')
    
def fnt_entradas(op):
    global existencias_arroz
    global existencias_queso
    global existencias_frijoles
    sw2 = True
    if op <1 or op >2:
        enter = input('\nOPCION NO VALIDA PRESIONE <ENTER> PARA CONTINUAR')
    elif op == 1:
        while sw2 == True:
            fnt_limpiarPantalla()
            opciones = int(input('\n---OPCION DE PRODUCTOS--- \n1. Arroz\n2. Queso\n3. Frijoles\n4. Salir\n -->'))
            if opciones == 4:
                sw2 = False
            if opciones >= 1 and opciones <= 3:
                cantidad = int(input('\nIngrese la Cantidad que desea agregar -> '))
                if opciones == 1:
                    existencias_arroz +=  cantidad
                if opciones == 2:
                    existencias_queso +=  cantidad
                if opciones == 3:
                    existencias_frijoles +=  cantidad
        
    
sw = True
while  sw == True:
    fnt_limpiarPantalla()
    opciones = int(input('\n---MENÚ DE OPCIONES---\n1. Registro de productos\n2. Salida de productos\n3.Salir\n --> '))
    fnt_entradas(opciones)