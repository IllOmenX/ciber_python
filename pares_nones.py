class Player:
    
    def __init__(self, equipo):
        self.equipo = equipo
    
        
while 1:
    equipo = input("Escoge pares o nones: ").lower()
    if equipo in ['pares', 'nones']:
        break
    else:
        print('Vuelva a intentarlo')

while 1:    
    try:
        num = int(input('Inserte un numero: '))
        if type(num).__name__ != int:
          break
    except ValueError:
        print('No has insertado un numero')
    

if num%2 == 0:
    print('El numero es par')
else:
    print('El numero es impar')


