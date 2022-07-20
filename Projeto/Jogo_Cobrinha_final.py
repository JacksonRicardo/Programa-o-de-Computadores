import pygame
from random import randint

pygame.init()

#Definindo cores em RGB
preto = 0, 0, 0
branco = 255, 255, 255
vermelho = 255, 0, 0
cinza_claro = 220, 220, 220


#Armazenamento do tamanho da tela em variáveis   
largura=640
altura=480


#Tamanho do objeto desenhado
tamanho_cobra = 10
tamanho_da_maça = 10


#Defino um relógio que conta o tempo do jogo
tempo = pygame.time.Clock()

#Criação da tela com a tamanho especificado
tela = pygame.display.set_mode((largura,altura))

#Pontuação
font = pygame.font.Font('freesansbold.ttf', 16)
pontos = 0

#Atualiza o nome da tela
pygame.display.set_caption("Jogo da Cobrinha")

def texto(mensagem, cor, tam, x, y):
    font = pygame.font.SysFont(None, tam)
    texto1 = font.render(mensagem, True, cor)
    tela.blit(texto1, [x, y])

def cobra(CobraXY):
    for XY in CobraXY:
        pygame.draw.rect(tela, preto, [XY[0], XY[1], tamanho_cobra, tamanho_cobra])

def maca(maca_x, maca_y):
    pygame.draw.rect(tela, vermelho, [maca_x, maca_y, tamanho_da_maça, tamanho_da_maça])

def jogo():
    #Loop para continuar rodando enquanto o evento QUIT não for detectado
    rodar = True
    fimdejogo = False
    pos_x = largura/2
    pos_y = altura/2
    #Definindo maça
    maca_x=randint(0,(largura-tamanho_da_maça)/10)*10
    maca_y=randint(0,(altura-tamanho_da_maça)/10)*10
    #Atribuindo velocidade
    velocidade_x=0
    velocidade_y=0
    CobraXY = []
    CobraComprimento = 1
    pontos = 0
    
    while rodar:
        while fimdejogo:
            tela.fill(branco)
            texto(("GAME OVER, aperte ESPAÇO para reiniciar"), preto, 30, largura/5, altura/2)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    rodar = False
                    fimdejogo = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        jogo()

                    
        #programa baseado em eventos!
        for event in pygame.event.get():
            #imprime os eventos para vizualização
            #print(event)
            if event.type == pygame.QUIT:
                rodar = False


            #Movimentando para a direita quando a seta da direita é pressionada    
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and velocidade_x != tamanho_cobra:
                    velocidade_y= 0
                    velocidade_x= - 10
                if event.key == pygame.K_RIGHT and velocidade_x != -tamanho_cobra:
                    velocidade_y=0
                    velocidade_x= 10
                if event.key == pygame.K_UP and velocidade_y != tamanho_cobra:
                    velocidade_x=0
                    velocidade_y= - 10
                if event.key == pygame.K_DOWN and velocidade_y != -tamanho_cobra:
                    velocidade_x = 0
                    velocidade_y = 10
                    
        #Preenche a tela com a cor verde
        tela.fill(cinza_claro)
        

    
        #Pega o valor da posição atual e fica aumentando em relação ao objeto    
        pos_x+=velocidade_x
        pos_y+=velocidade_y
        

        #Criando lista para cobra
        CobraInicio = []
        CobraInicio.append(pos_x)
        CobraInicio.append(pos_y)
        CobraXY.append(CobraInicio)
        if len(CobraXY) > CobraComprimento:
            del CobraXY[0]
        if any(Bloco == CobraInicio for Bloco in CobraXY[:-1]):
            fimdejogo = True

        #Definindo posição da pontuação, nome e cor
        pontos_font = font.render('Maças Comidas: %s' % (pontos), True, preto)
        pontos_rect = pontos_font.get_rect()
        pontos_rect.topleft = (600 - 120, 10)
        tela.blit(pontos_font, pontos_rect)
            

        #Chamando a Cobra
        cobra(CobraXY)
        if pos_x == maca_x and pos_y == maca_y:
            maca_x=randint(0,(largura-tamanho_da_maça)/10)*10
            maca_y=randint(0,(altura-tamanho_da_maça)/10)*10
            CobraComprimento += 1
            
            pontos += 1
        
        maca(maca_x,maca_y)

        #Atualiza o display
        pygame.display.update()
        #20 frames por segundo
        tempo.tick(13)


        #Definindo Bordas
        if pos_x > largura:
            fimdejogo = True
        if pos_x < 0:
            fimdejogo = True
        if pos_y > altura:
            fimdejogo = True
        if pos_y < 0:
            fimdejogo = True

#Chamando função jogo    
jogo()

#Encerra o pygame
pygame.quit()
