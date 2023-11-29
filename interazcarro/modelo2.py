import pygame
import piloto
import copiloto
orange = '#dc4e0c'
blue = '#061a2a'
white = (244, 245, 247)
gold = (215, 166, 75)
red = (199, 33, 56)


class indice:
    def __init__(self, screen, default_color=orange):
        self.screen = screen
        self.size = self.screen.get_size()
        self.default_color = default_color
        self.getimages()
        self.center = [35, self.size[1]/2]

        self.stados = [0, 0, 0, 0]
        self.Ui = [None, None, None, None]
        self.Ui[3] = piloto.piloto(self.screen, self.center, default_color=default_color)
        self.Ui[1] = copiloto.piloto(self.screen, self.center, default_color=default_color)
        self.centerd = [100, 400]
        self.centern = [150, 400]
        self.centerr = [200, 400]

    def getimages(self):
        self.images = [None, None, None]
        img = pygame.image.load('imagenes/robotBlanco.png').convert()
        img.convert_alpha()
        img.set_colorkey(0)
        img = pygame.transform.scale(img, (35, 35))
        self.images[0] = img

        img = pygame.image.load('imagenes/mapaBlanco.png').convert()
        img.convert_alpha()
        img.set_colorkey(0)
        img = pygame.transform.scale(img, (35, 35))
        self.images[1] = img

        img = pygame.image.load('imagenes/control.png').convert()
        img.convert_alpha()
        img.set_colorkey(0)
        img = pygame.transform.scale(img, (35, 35))
        self.images[2] = img

        self.rect = [None, None, None]

        self.rect[0] = self.images[0].get_rect()
        self.rect[1] = self.images[1].get_rect()
        self.rect[2] = self.images[2].get_rect()

    def dibujar(self):
        # dibujas lineas
        self.rect[0].center = (self.center[0], self.center[1])
        self.screen.blit(self.images[0], self.rect[0])

        self.rect[1].center = (self.center[0], self.center[1]+70)
        self.screen.blit(self.images[1], self.rect[1])
        self.dibujar_lineas()

        self.rect[2].center = (self.center[0], self.center[1]-70)
        self.screen.blit(self.images[2], self.rect[2])

        self.dibujar_gui()

        self.dibujardnr()

    def dibujardnr(self):
        font = pygame.font.Font('yagora.ttf', 40)
        text = font.render('D', True, blue, self.default_color)
        text2 = font.render('N', True, blue, self.default_color)
        text3 = font.render('R', True, blue, self.default_color)

        textcenter = text.get_rect()
        textcenter2 = text2.get_rect()
        textcenter3 = text3.get_rect()

        textcenter.center = self.centerd
        textcenter2.center = self.centern
        textcenter3.center = self.centerr

        self.screen.blit(text,textcenter)
        self.screen.blit(text2, textcenter2)
        self.screen.blit(text3, textcenter3)

    def dibujar_lineas(self):

        pygame.draw.line(self.screen, pygame.Color(self.default_color),
                         (self.center[0]-20, self.center[1]+35), (self.center[0]+25, self.center[1]+35))
        pygame.draw.line(self.screen, pygame.Color(self.default_color),
                         (self.center[0] - 20, self.center[1] - 35), (self.center[0] + 25, self.center[1] - 35))

    def expandir(self, simbolo):
        if self.Ui[simbolo] is not None:
            self.Ui[simbolo].expandir()
            self.stados[simbolo] = True
        if simbolo == 3:
            self.set_color(orange)
        if simbolo == 1:
            self.set_color(gold)

    def retraer(self, simbolo):
        self.Ui[simbolo].retraer()
        self.stados[simbolo] = False
        if simbolo == 3 or simbolo == 1:
            self.set_color(white)

    def animar (self, simbolo):
        if simbolo != 0:
            if self.stados[simbolo] == True:
                self.retraer(simbolo)
                return 0
            elif self.stados[simbolo] == False:
                self.expandir(simbolo)
                return simbolo

    def getsimbol(self,pos):
        s = 0
        if ((pos[0] < (self.rect[0].center[0]+35) and (pos[0] > self.rect[0].center[0]-35))
        and (pos[1] < (self.rect[0].center[1]+35) and pos[1] > (self.rect[0].center[1]-35))):
            s = 1
        elif ((pos[0] < (self.rect[1].center[0]+35) and (pos[0] > self.rect[1].center[0]-35))
        and (pos[1] < (self.rect[1].center[1]+35) and pos[1] > (self.rect[1].center[1]-35))):
            s = 2
        elif ((pos[0] < (self.rect[2].center[0]+35) and (pos[0] > self.rect[2].center[0]-35))
        and (pos[1] < (self.rect[2].center[1]+35) and pos[1] > (self.rect[2].center[1]-35))):
            s = 3
        elif (((pos[0] < self.centerd[0]+35) and (pos[0] > self.centerd[0]-35))
        and ((pos[1] < self.centerd[1]+35) and (pos[1] > self.centerd[1]-35))):
            s = 7
        elif (((pos[0] < self.centern[0]+35) and (pos[0] > self.centern[0]-35))
        and ((pos[1] < self.centern[1]+35) and (pos[1] > self.centern[1]-35))):
            s = 8
        elif (((pos[0] < self.centerr[0]+35) and (pos[0] > self.centerr[0]-35))
        and ((pos[1] < self.centerr[1]+35) and (pos[1] > self.centerr[1]-35))):
            s = 9
        else:
            n = self.Ui[3].get_button(pos)
            if n != False:
                s = n


        return s

    def dibujar_gui(self):
        self.Ui[3].dibujar()
        self.Ui[1].dibujar()


    def get_active(self):
        speed = self.get_speed()
        return self.stados[1], speed

    def set_color(self,color):
        self.default_color = color
        self.Ui[3].default_color = color
        self.Ui[1].default_color = color
