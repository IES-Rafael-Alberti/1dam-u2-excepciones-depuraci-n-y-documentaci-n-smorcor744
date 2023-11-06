"""
Actividad 2: 
    Reescribe el programa conversor de temperaturas para que lea repetidamente la temperatura hasta que sea correcta, debe detectar los fallos usando try y except.
"""

def temp(ent: str):
    mal = False
    while not mal:
        ent = input('Introduzca la Temperatura Fahrenheit:')

        try:
            fahr = float(ent)
            cel = (fahr - 32.0) * 5.0 / 9.0
            print(cel)
        except ValueError:
            ent = input('Introduzca la Temperatura Fahrenheit:') 
        else:
            return cel

    """Solicita una temperatura

            Args:
                fahr = float(ent): comprueba si la temperatura esta bien puesta.
                cel = (fahr - 32.0) * 5.0 / 9.0: covierte la temperatura 
                print(cel): muestra la temperatura

            except ValueError:
                ent : si no se puede convertir en float pregunta otra vez

    
    Returns:
        cel : conversión
    """

ent = input('Introduzca la Temperatura Fahrenheit:')
temp(ent)