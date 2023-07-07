import pygame
import random
pygame.init()
bluepen=pygame.image.load('bluepen.png')
bluepeninvertido=pygame.transform.flip(bluepen,True,False)
player=bluepen
redpen=pygame.image.load('redpen.png')
fundo=pygame.image.load('bg.png')
tamanho=(800,600)
clock=pygame.time.Clock()
tela=pygame.display.set_mode(tamanho)
icon=pygame.image.load('bluepen.ico')
pygame.display.set_icon(icon)
pygame.display.set_caption('Blue Pen x Red Pen')
running=True
posicaoXblue=400
posicaoYblue=300
movimentoXblue=0
movimentoYblue=0
posicaoXred=1
posicaoYred=300
velocidade=1
direita=True
while running:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT or evento.type==pygame.KEYDOWN and evento.key==pygame.K_ESCAPE:
            running=False
        elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_LEFT:
            movimentoXblue=-5
            player=bluepen
        elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_RIGHT:
            movimentoXblue=5
            player=bluepeninvertido
        elif evento.type==pygame.KEYUP and evento.key==pygame.K_LEFT or evento.type==pygame.KEYUP and evento.key==pygame.K_RIGHT:
            movimentoXblue=0
        elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_UP:
            movimentoYblue=-5
        elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_DOWN:
            movimentoYblue=5
        elif evento.type==pygame.KEYUP and evento.key==pygame.K_UP or evento.type==pygame.KEYUP and evento.key==pygame.K_DOWN:
            movimentoYblue=0
    tela.blit(fundo,(0,0))
    tela.blit(player,(posicaoXblue,posicaoYblue))
    tela.blit(redpen,(posicaoXred,posicaoYred))
    posicaoXblue=posicaoXblue+movimentoXblue
    posicaoYblue=posicaoYblue+movimentoYblue
    if posicaoXblue>=710:
        posicaoXblue=710
    elif posicaoXblue<=0:
        posicaoXblue=0
    if posicaoYblue>=500:
        posicaoYblue=500
    elif posicaoYblue<=0:
        posicaoYblue=0
    if posicaoXred>=800:
        direita=False
        redpen=pygame.transform.flip(redpen,True,False)
        velocidade=velocidade+1
        posicaoYred=random.randint(0,600)
    elif posicaoXred<=-100:
        direita=True
        redpen=pygame.transform.flip(redpen,True,False)
        velocidade=velocidade+1
        posicaoYred=random.randint(0,600)
    if direita:
        posicaoXred=posicaoXred+velocidade
    else:
        posicaoXred=posicaoXred-velocidade
    pygame.display.update()
    clock.tick(60)