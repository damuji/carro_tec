import pygame

orange = (224, 98, 54)
blue = (48, 76, 122)
white = (244, 245, 247)
gold = (215, 166, 75)
red = (199, 33, 56)


class Pedal:
    def __init__(self, pos, largo):
        self.pos = pos
        self.largo = largo
        self.posf = (self.pos[0]+self.largo, self.pos[1])

    def dibujar(self, screen, pedal, color=(224, 98, 54)):
        pygame.draw.line(screen, color, self.pos, self.posf, 2)

        # se pone el letrero de threshold
        texto = pygame.font.Font('freesansbold.ttf', 8)
        text = texto.render('Threshold', True, blue, color)
        textrect = text.get_rect()
        textrect.center = (self.pos[0] - 3, self.pos[1] - 45)
        screen.blit(text, textrect)

        # se pone el el indicador de threshold

        pygame.draw.rect(screen, pygame.Color(color), (self.pos[0], self.pos[1]-10, (pedal/100)*self.largo, 10), 0)
