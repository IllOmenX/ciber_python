
#Importamos librerias
import random
import difflib

#Definimos funciones
def enunciado():
    print("""
    Juego de Piedra, Papel y Tijeras en Python
    En este programa, jugarás contra la computadora en el clásico juego de Piedra, Papel y Tijeras.
    Elige tu jugada, compite con la computadora y descubre quién gana cada ronda.
    ¡Diviértete y buena suerte!
    """)
    

def player():
    """Este será el jugador humano

    Returns:
        string: La opcion elegida
    """
    
    print("Turno jugador...")
    opciones = ["piedra", "papel", "tijeras"]
    
    while True : #Hacemos un bucle por si el jugador no escoge una opcion valida
        
        eleccion = input("Elige opcion: ").lower()  #Con .lower() evitamos errores poninendo todo el input a minúsculas
        
        try:
            most_similar_option = difflib.get_close_matches(eleccion, opciones, n=1)
            
            if most_similar_option[0] in opciones:    #Si el input coincide con alguna opción se saldrá del bucle
                print(f'Has escogido {most_similar_option[0]}')
                return most_similar_option[0]
        except:
            print('Eleccion no valida, vuelva a intentarlo')
        
def maquina():
    """Este será el jugador robot

    Returns:
        string: La opcion elegida
    """
    
    print("Turno maquina...")
    opciones = ["piedra", "papel", "tijeras"]
    aleatorio = random.choice(opciones)
    print('La maquina ha escogido: ' + aleatorio)
    
    return aleatorio
        
def juego(jugador, maquina):
    """_summary_

    Args:
        jugador player(): jugador creado anteriormente
        maquina maquina(): maquina creada anteriormente

    Returns:
        int: Suma de punto
    """
    
    # Definimos las reglas
    reglas = {
        #Gana   |   Pierde
        "piedra": "tijeras",
        "papel": "piedra",
        "tijeras": "papel"
    }
    
    # Si el jugador ha elegido lo mismo que la maquina, Empate
    if jugador == maquina:
        print("Empate")
        return 0 # Devolvemos 0 porque no hay punto
    
    # Si el la el valor con la key de jugador coincide con la de maquina, quiere decir que gana jugador
    elif reglas[jugador] == maquina:
        print("Punto para jugador")
        return 1 # Sumamos un punto al jugador al devolver 1
    
    #Si no ocurre nada de lo anterior, gana la maquina
    else:
        print("Punto para maquina")
        return 2 # Sumamos un punto al la maquina cuando retornamos 2


### Comienza el programa
enunciado()

#Eleccion de rondas
while 1:
    rondas = int(input("Al mejor de cuantas rondas se va a jugar?\nRecuerde que debe ser impar para no quedar en empate: "))
    if rondas % 2 == 1:
        break
    else:
        print("No es impar")
        print()


# Contador de victorias
v_jugador = 0
v_maquina = 0

while 1:
    j_player = player() # Juega el jugador
    j_maquina = maquina() # Juega la maquina
    resultado = juego(j_player, j_maquina)
    print('------')
    if resultado == 1:
        v_jugador += 1
        
        if v_jugador > (rondas/2):
            print("El jugador ha ganado")
            exit()
                   
    elif resultado == 2:
        v_maquina += 1
        
        if v_maquina> (rondas/2):
            print("La maquina ha ganado")
            exit()
    

