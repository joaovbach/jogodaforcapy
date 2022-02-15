import sys, pygame

pygame.init()

screen = pygame.display.set_mode([500,500])
palavra = ""
posicoesCertas = []
letrasCertas = []
jogando = False
tentativas = 0
adivinhando = False
palavraChute = ""

posicaoLetraChute = [0,tentativas*60]

def render(first,chute):
    x = 0
    y = tentativas*60
    if first:
        for i in palavra:
            pygame.draw.rect(screen,[255,0,0],[x,y,40,40])
            x+=50
    else:
        for i in range(0,len(chute)):
            if chute[i] in palavra:
                if chute[i] == palavra[i]:
                    pygame.draw.rect(screen,[255,255,0],[x,y,40,40])
                else:
                    pygame.draw.rect(screen,[255,100,255],[x,y,40,40])
            else:
                pygame.draw.rect(screen,[255,0,0],[x,y,40,40])

            x+=50

        palavraChute = ""
        adivinhando=True
        

def renderchute(word):
    xChute = 0
    for i in word:
        pygame.draw.rect(screen,[255,255,255],[xChute,360,40,40])
        xChute+=50

def renderPalavraChute(word):
    xChute = 0
    for i in word:
        pygame.draw.rect(screen,[255,255,255],[xChute,360,40,40])

        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(i, False, (0, 0, 0))
        screen.blit(textsurface,(xChute,360))

        xChute+=50

def cleanScreen():
    pygame.draw.rect(screen,[0,0,0],[0,0,1000,1000])

def verificaPalavra(word):
    pass


while 1:
    if jogando == False:
        palavra = "joao bach"
        render(True,"")
        jogando=True
        adivinhando=True
        renderchute(palavra)
    else:
        pass

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if adivinhando == True:
                if len(palavraChute)<len(palavra):
                    if event.key == pygame.K_BACKSPACE:
                        palavraChute = palavraChute[:-1:]
                        renderchute(palavra)
                        renderPalavraChute(palavraChute)
                    else:
                        palavraChute += str(chr(event.key))
                        renderchute(palavra)
                        renderPalavraChute(palavraChute)
                else:
                    print("aperte enter para seguir")

            if event.key == pygame.K_0:
                tentativas+=1
                render()

            if event.key == pygame.K_2:
                print("ola")
                if adivinhando:
                    if len(palavraChute) >= len(palavra):
                        #adivinhando=False
                        tentativas+=1
                        render(False, palavraChute)
                        renderchute(palavra)
                        palavraChute=""



    pygame.display.update()