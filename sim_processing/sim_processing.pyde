x, y, vx, vy = 200, 200, 0, 0
posX_l1, posX_l2, posX_l3 = -5, 0, 5
posY_l1, posY_l2, posY_l3 =  0, 0, 0
pista = [(200, 200), (200, 600), (600, 600), (600, 200)] #TODO alterar para pontos aleatorios
pista.append(pista[0])

import robo, pista_tela
carro = robo.robo(205, 300)

def setup():
    size(800, 800)

def draw():
    global estado, x, y, vx, vy
    pista_tela.desenha_pista(pista)
    carro.controle()
    carro.desenha()