import pedal
import velocimetro
import pygame
import math
orange = '#dc4e0c'
blue = '#061a2a'
white = (244, 245, 247)
gold = (215, 166, 75)
red = (199, 33, 56)


class Tablero:
    def __init__(self, screen, default_color=orange):
        self.vel = velocimetro.Veloc(100, 1, 0, 120, (600, 150), default_color)
        self.ped = pedal.Pedal((502, 325), 200)
        self.screen = screen
        self.size = self.screen.get_size()
        self.default_color = default_color
        self.box = [self.size[0] - self.size[0] * .40, self.size[1] * .05]
        self.lengh = self.size[0]*.30
        self.hight = self.size[1] * .50

        # variables para el velocimetro
        self.pos = [self.box[0]+self.lengh/2, self.box[1]+self.hight/2]
        self.tamano = self.hight*.75/2
        self.font = int(self.hight*.045)
        self.font2 = 10

        # variables para el pedal
        self.hightp = self.hight*.25
        self.posf = [self.box[0]+self.lengh*.75+self.hight*.12, self.box[1]+self.hight+self.hightp]
        self.vel = 0

    def dibujarvel(self):

        self.writelegend1()
        self.velocimetro()

    def writelegend1(self):
        pygame.draw.line(self.screen, pygame.Color(self.default_color), (self.box[0], self.box[1]),
                         (self.box[0] + self.lengh, self.box[1]), 1)

        text = pygame.font.Font('yagora.ttf', self.font2)
        text1 = text.render('Speed', True, blue, self.default_color)

        reac = text1.get_rect()
        reac.center = (self.box[0], self.box[1]+self.font2/2)

        self.screen.blit(text1, reac)

    def writelegend2(self):
        pygame.draw.line(self.screen, pygame.Color(self.default_color), (self.box[0], self.box[1] + self.hight),
                         (720, self.box[1] + self.hight), 1)

        text = pygame.font.Font('yagora.ttf', self.font2)
        text2 = text.render('Pedal', True, blue, self.default_color)

        reac2 = text2.get_rect()
        reac2.center = (self.box[0], self.box[1] + self.hight + self.font2 / 2)

        self.screen.blit(text2, reac2)

    def velocimetro(self):
        pos = self.pos

        pygame.draw.circle(self.screen, pygame.Color(self.default_color), pos, self.tamano, 1)

        deg = math.radians(220 - (self.vel * 2.6))

        posx = (self.tamano - 1) * math.cos(deg) + pos[0]
        posy = (self.tamano + 1) * math.sin(deg) * -1 + pos[1]

        # se pone el letrero de velocidad
        self.velocimetrodigital(self.vel)

        # circulo externo
        self.circuloexter()

        # se dibuja el circulo de la velocidad
        pygame.draw.circle(self.screen, pygame.Color(self.default_color), (posx, posy), self.tamano / 10, 1)
        pygame.draw.circle(self.screen, pygame.Color(blue), (posx, posy), self.tamano / 10 - 1, 0)

    def velocimetrodigital(self, vel):
        ofset = 5
        if vel >= 10:
            ofset = -10
        elif vel >= 100:
            ofset = -30
        elif vel == 11:
            ofset = 0

        font = pygame.font.Font('yagora.ttf', self.font*4)
        font2 = pygame.font.Font('yagora.ttf', self.font)

        text = font.render(str(int(vel)), True, self.default_color)
        text2 = font2.render('km/h', True, blue, self.default_color)

        textrect = text.get_rect()
        textrect2 = text2.get_rect()

        textrect.center = (self.pos[0] + ofset, self.pos[1] )
        textrect2.center = (self.pos[0] + 30, self.pos[1] + 10 )

        self.screen.blit(text, textrect)
        self.screen.blit(text2, textrect2)

    def circuloexter(self):
        dot_size = 5
        extra = (self.tamano/10)*1.50
        circle_center = (self.pos[0], self.pos[1])
        circle_radius = self.tamano + extra
        for angle in range(0, 360, dot_size):
            x = circle_center[0] + circle_radius * math.cos(angle * (3.14159 / 180))
            y = circle_center[1] + circle_radius * math.sin(angle * (3.14159 / 180))
            pygame.draw.circle(self.screen, self.default_color, (x, y), 1.2)  # 1 es el radio del punto

    def sethight(self, hight):
        self.hight = hight
        self.pos = [self.box[0] + self.lengh / 2, self.box[1] + self.hight / 2]
        self.tamano = self.hight * .75 / 2
        self.font = int(self.hight * .045)
        self.posf = [self.box[0] + self.lengh * .75 + self.hight * .12, self.box[1] + self.hight + self.hightp]

    def dibujarpedal(self, ped=1):

        pygame.draw.line(self.screen, self.default_color, (self.box[0]+self.hight*.12, self.posf[1]), self.posf, 2)
        pygame.draw.rect(self.screen, self.default_color, (self.box[0] + self.hight * .121, self.posf[1] - 10,
                                                           (ped / 100) * self.lengh * .755, 10),
                         0)

        self.writelegend2()
