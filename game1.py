import pygame
pygame.init()

#variaveis globais
loop=True

janela = pygame.display.set_mode([1080,720])
titulo = pygame.display.set_caption("jogo")
xarope =pygame.image.load("./imagens/xarope.png")
velocidade= 0.5
px = 10
py = 10

a=False
w=False
s=False
d=False

def events():
    global loop, px,py, velocidade, a,d,s,w
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            loop=False
        if evento.type ==pygame.KEYDOWN:
            if evento.key == pygame.K_s:
                s=True
            if evento.key == pygame.K_w:
                w=True
            if evento.key == pygame.K_a:
                a=True
            if evento.key == pygame.K_d:
                d=True
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_s:
                s=False
            if evento.key == pygame.K_w:
                w=False
            if evento.key == pygame.K_a:
                a=False
            if evento.key == pygame.K_d:
                d=False

def xarope_():
    global xarope,a,s,d,w,px,py,velocidade

    janela.blit(xarope, [px, py])

    if a:
        px-=velocidade
        if(px <=0):
            px = 0
    if d:
        px+= velocidade
        if (px >= 980):
             px=980
    if w:
        py-=velocidade
        if (px >= 980):
             px=0
    if s:
        py+= velocidade
        if (px >= 0):
             px=0