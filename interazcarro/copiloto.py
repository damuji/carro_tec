import pygame
import piloto
orange = '#dc4e0c'
blue = '#061a2a'
white = (244, 245, 247)
gold = (215, 166, 75)
red = (199, 33, 56)
class piloto(piloto.piloto):
    def dibujar(self):
        if self.expaniendo == True:
            self.Dexpandir()
        if self.retrae == True:
            self.Dretraer()
        if self.closed != True:
            pygame.draw.line(self.screen, pygame.Color(self.default_color),
                             (self.center[0] - 20, self.center[1] + 35),
                             (self.center[0] + self.line, self.center[1] + 35))
            if self.end[0] == True :
                font = pygame.font.Font('yagora.ttf', 60)
                text = font.render('+', True, blue, self.default_color)
                text2 = font.render('-', True, blue, self.default_color)
                text3 = font.render(str(self.set_speed), True, blue, self.default_color)



