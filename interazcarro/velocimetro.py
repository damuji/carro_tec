import pygame.draw
import pygame.font
import math

orange = (224, 98, 54)
blue = (48, 76, 122)
white = (244, 245, 247)
gold = (215, 166, 75)
red = (199, 33, 56)


class Veloc:
    def __init__(self, tamano, ancho, minimo, maximo, pos, color=(224, 98, 54)):
        self.tamano = tamano
        self.ancho = ancho
        self.min = minimo
        self.max = maximo
        self.pos = pos


        self.font = pygame.font.Font('freesansbold.ttf', 40)
        self.text = self.font.render('10', True, (224, 98, 54))
        self.font2 = pygame.font.Font('freesansbold.ttf', 10)
        self.text2 = self.font2.render('km/h', True, (48, 76, 122), color)
        self.textRect = self.text.get_rect()
        self.textRect2 = self.text2.get_rect()
        self.ofset = 8
        self.textpos = [self.pos[0], self.pos[1] + self.ofset]
        self.textRect.center = (self.textpos[0], self.textpos[1])
        self.textRect2.center = (self.pos[0] + 30, self.pos[1] + 10 + self.ofset)

    def pointcircle(self, screen, color=(224, 98, 54)):
        dot_size = 5
        extra = 15
        circle_center = (self.pos[0], self.pos[1])
        circle_radius = self.tamano + extra
        for angle in range(0, 360, dot_size):
            x = circle_center[0] + circle_radius * math.cos(angle * (3.14159 / 180))
            y = circle_center[1] + circle_radius * math.sin(angle * (3.14159 / 180))
            pygame.draw.circle(screen, color, (x, y), 1.2)  # 1 es el radio del punto

    def draw(self, vel, screen, color=(224, 98, 54)):
        pos = self.pos
        pygame.draw.circle(screen, pygame.Color(color), pos, self.tamano, self.ancho)

        deg = math.radians(220 - (vel * 2.6))

        posx = (self.tamano - self.ancho) * math.cos(deg) + pos[0]
        posy = (self.tamano + self.ancho) * math.sin(deg) * -1 + pos[1]

        # se pone el letrero de velocidad
        self.text = self.font.render(str(vel), True, color)

        # se dibuja el circulo de la velocidad
        pygame.draw.circle(screen, pygame.Color(color), (posx, posy), self.tamano / 10, self.ancho)
        pygame.draw.circle(screen, pygame.Color((48, 76, 122)), (posx, posy), self.tamano / 10 - self.ancho, 0)
        extra = 0
        if vel >= 10:
            extra = -6
        if vel >= 100:
            extra = -30
        if vel < 10:
            extra = 15
        if vel == 11:
            extra = 0
        self.textRect.center = (self.textpos[0] + extra, self.textpos[1])
        self.pointcircle(screen, color)

        texto = pygame.font.Font('freesansbold.ttf', 8)
        text = texto.render('speed', True, blue, color)
        textrect = text.get_rect()
        textrect.center = (self.pos[0] - 115, self.pos[1] - 121)
        screen.blit(text, textrect)

        # ponerl el letrerito de km/h
        texto2 = pygame.font.Font('freesansbold.ttf', 15)
        text2 = texto2.render('100', True, color)
        textrect2 = text2.get_rect()
        textrect2.center = (self.pos[0] + 100, self.pos[1] + 90)

        screen.blit(text2, textrect2)
        screen.blit(self.text, self.textRect)
        screen.blit(self.text2, self.textRect2)
