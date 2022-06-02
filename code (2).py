import board
from digitalio import DigitalInOut, Direction, Pull
import time


# Configuration des entrées sorties
feu1V = DigitalInOut(board.GP18)
feu1V.direction = Direction.OUTPUT
feu1O = DigitalInOut(board.GP17)
feu1O.direction = Direction.OUTPUT
feu1R = DigitalInOut(board.GP16)
feu1R.direction = Direction.OUTPUT
bpiet1 = DigitalInOut(board.GP12)
bpiet1.direction = Direction.INPUT
bpiet1.pull = Pull.UP
bpiet2 = DigitalInOut(board.GP11)
bpiet2.direction = Direction.INPUT
bpiet2.pull = Pull.UP
bmag = DigitalInOut(board.GP13)
bmag.direction = Direction.INPUT
bmag.pull = Pull.UP

# ▓ Initialisation de l'automate
X0 = 1
X10 = 0
X20 = 0
Q1 = False
tempo = 0
while True:
    # Déterminer la valeur de la sortie de la temporisation
    if X10 == 1 :
        if tempo ==0 :
            t =time.monotonic()
            tempo = 1
            Q1 = 0
        if time.monotonic()-t > 3 :
            Q1 =True
            tempo = 0
            print(tempo)


    # Les conditions d'évolution
    CE0_10 = not bpiet1.value and X0
    CE10_20 = Q1 and X10
    CE20_0 = not bmag.value and X20

    # Les étapes
    if CE0_10:
        X10 = 1
        X0 = 0
    if CE10_20:
        X20=1
        X10=0
    if CE20_0:
        X0 = 1
        X20 = 0
    # Les actions
    feu1V.value = X0
    feu1O.value = X10
    feu1R.value = X20
