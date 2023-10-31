import random

win = """
        Ganaste! No tan rapido. Quiero la revancha
      """
    
emp = """
        Empatamos... jugamos otra?
      """
    
lost = """
        Perdiste, segui participando
       """

def piedra(opc):
    compu = ["piedra", "papel", "tijera"]
    juego = random.choice(compu)
    
    if opc == "piedra" and juego == "piedra":
        print(emp)
        
    elif opc == "piedra" and juego== "papel":
        print(lost)
        
    elif opc == "piedra" and juego == "tijera":
        print(win)
    run()

def papel(opc):
    compu = ["piedra", "papel", "tijera"]
    juego = random.choice(compu)
    
    if opc == "papel" and juego == "piedra":
        print(win)
        
    elif opc == "papel" and juego== "papel":
        print(emp)
        
    elif opc == "piedra" and juego == "tijera":
        print(lost)
    run()

def tijera(opc):
    compu = ["piedra", "papel", "tijera"]
    juego = random.choice(compu)
    
    if opc == "tijera" and juego == "piedra":
        print(lost)
        
    elif opc == "tijera" and juego== "papel":
        print(win)
        
    elif opc == "tijera" and juego == "tijera":
        print(emp)
    run()
    
def run():
    
    texto = """Elige una opcion:
    1 - Piedra.
    2 - Papel.
    3 - Tijera.
    4 - Finalizar juego.
    
    presiona el numero de la opcion: """
    
    inp = int(input(texto))
    
    if inp == 1:
        piedra("piedra")
    elif inp == 2:
        papel("papel")
    elif inp == 3:
        tijera("tijera")
    elif inp == 4:
        print("El juego ha finalizado. Nos vemos pronto")
    else:
        print("la opcion no es valida. por favor, escribe el numero de la opcion")
    run()

if __name__ == '__main__':

    run()