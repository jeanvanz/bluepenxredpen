import pygame
pygame.init()
bluepen=pygame.image.load('bluepen.png')
redpen=pygame.image.load('redpen.png')
fundo=pygame.image.load('bg.png')
tamanho=(800,600)
clock=pygame.time.Clock()
tela=pygame.display.set_mode(tamanho)
pygame.display.set_icon(bluepen)
pygame.display.set_caption('Blue Pen x Red Pen')
running=True
posicaoXblue=400
posicaoYblue=300
posicaoXred=100
posicaoYred=300
while running:
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT or evento.type==pygame.KEYDOWN and evento.key==pygame.K_ESCAPE:
            running=False
    tela.blit(fundo,(0,0))
    tela.blit(bluepen,(posicaoXblue,posicaoYblue))
    tela.blit(redpen,(posicaoXred,posicaoYred))
    pygame.display.update()
    clock.tick(60)