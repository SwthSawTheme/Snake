import pygame
import random

pygame.init()
pygame.display.set_caption("Snake Game - by Saw Theme")

largura, altura = 720,480
relogio = pygame.time.Clock()
display = pygame.display.set_mode((largura,altura))

preto = (0,0,0)
azul = (0,0,255)
branco = (255,255,255)
vermelho = (255,0,0)

quadrado = 20

def desenhar_comida(quadrado,comida_x,comida_y):
    pygame.draw.rect(display,azul,[comida_x,comida_y,quadrado,quadrado])

def desenhar_cobra(quadrado,pixels):
    for pixel in pixels:
        pygame.draw.rect(display,vermelho,[pixel[0],pixel[1],quadrado,quadrado])

def gerar_comida():
    comida_x = round(random.randrange(0,largura - quadrado) / quadrado) * quadrado
    comida_y = round(random.randrange(0,altura - quadrado) / quadrado) * quadrado 
    return comida_x, comida_y

def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica",22)
    texto = fonte.render(f"Pontos: {pontuacao}",True,branco)
    display.blit(texto,[2,2])

def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        vel_x = 0
        vel_y = quadrado
    elif tecla == pygame.K_UP:
        vel_x = 0
        vel_y = - quadrado
    elif tecla == pygame.K_LEFT:
        vel_x = - quadrado
        vel_y = 0
    elif tecla == pygame.K_RIGHT:
        vel_x = quadrado
        vel_y = 0
    return vel_x, vel_y

def game():
    fps = 10
    fim_jogo = False
    
    x = largura / 2
    y = altura / 2
    
    vel_x = 0
    vel_y = 0
    
    tamanho_cobra = 1
    pixels = []
    
    comida_x, comida_y = gerar_comida()
    
    while not fim_jogo:
        #define a cor da tela
        display.fill(preto)
        #desenha a comida na tela do jogo, de forma aleatoria
        desenhar_comida(quadrado,comida_x,comida_y)
        
        #evento responsável pelo incerramento do jogo, caso feche a janela
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                vel_x, vel_y = selecionar_velocidade(evento.key)
         
        #logica responsavel pelo "andar" da cobra        
        pixels.append([x,y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        
        #logica responsavel pelo fim do jogo caso a cobra encoste no próprio corpo
        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                fim_jogo = True
                
        # Define a posição para a extrema direita da tela
        if x < 0:
            x = largura - quadrado
        # Define a posição para o extremo esquerdo da tela
        elif x >= largura:
            x = 0
        elif y < 0:
            y = altura - quadrado
        elif y >= altura:
            y = 0
        
            
        x += vel_x
        y += vel_y
        
        desenhar_cobra(quadrado,pixels)
        desenhar_pontuacao(tamanho_cobra - 1)
                
        pygame.display.update()
        
        #Acrescentar 1 comida após comer outra
        if x == comida_x and y == comida_y:
            tamanho_cobra += 1
            fps += 1
            comida_x, comida_y = gerar_comida()
        
        relogio.tick(fps)
        


game()