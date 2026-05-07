import random


def obtener_palabra_secreta() -> str:
    palabras= ['python', 'javascript', 'java', 'angular', 'django', 'tensorflow', 'react', 'typescript', 'git', 'flask']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado -= "_"
    return adivinado

def juego_ahorcado():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 7
    juego_terminado = False

    print("Bienvenido al juego del ahorcado")
    print(f"Tienes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas))

    
