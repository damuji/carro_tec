import pygame
orange = '#dc4e0c'
blue = '#061a2a'
white = (244, 245, 247)
gold = (215, 166, 75)
red = (199, 33, 56)
class piloto:
    def __init__(self,screen,line, default_color=orange):
        self.closed = True
        self.screen = screen
        self.expaniendo = False
        self.time = 0
        self.center = line
        self.line = 35
        self.default_color = default_color
        self.retrae = False
        self.end = [False,False]
        self.set_speed = 0

    def expandir(self):
        self.expaniendo = True
        self.closed = False
        self.retrae = False
        self.end[0] = False

    def Dexpandir(self):
        if self.time < 30 and self.line < 350:
            self.time += 1
            self.line +=14
        else:
            self.end[0] = True

    def retraer (self):
        self.expaniendo = False
        self.retrae = True
        self.set_speed = 0

    def Dretraer (self):
        if self.time > 0 and self.line > 0:
            self.time -= 1
            self.line -=14
        else:
            self.closed = True

    def get_button (self,pos):
        if self.closed == False:
            if ((self.center[0] + (self.line/4) - 20 < pos[0] < (self.center[0] + (self.line/4)+20))
                    and (self.center[1] - 35- 100 < pos[1] < self.center[1]- 100 + 35)):
                if self.set_speed > 0:
                    self.set_speed -= 1
                return 4
            elif ((self.center[0] + (self.line/4*3) - 20 < pos[0] < (self.center[0] + (self.line/4*3)+20))
                    and (self.center[1] - 35- 100 < pos[1] < self.center[1]- 100 + 35)):
                if self.set_speed < 120:
                    self.set_speed += 1
                    return 5
            else:
                return False
        else:
            return False

    def dibujar(self):
        if self.expaniendo == True:
            self.Dexpandir()
        if self.retrae == True:
            self.Dretraer()
        if self.closed != True:
            pygame.draw.line(self.screen, pygame.Color(self.default_color),
                             (self.center[0] - 20, self.center[1] - 35),
                             (self.center[0] + self.line, self.center[1] - 35))
            if self.end[0] == True :
                font = pygame.font.Font('yagora.ttf', 60)
                text = font.render('+', True, blue, self.default_color)
                text2 = font.render('-', True, blue, self.default_color)
                text3 = font.render(str(self.set_speed), True, blue, self.default_color)

                textrect2 = text.get_rect()
                textrect2.center = (self.center[0] + self.line/4, self.center[1] - 100)


                textrect = text2.get_rect()
                textrect.center = (self.center[0] + (self.line/4*3), self.center[1] -100)

                text3rect = text3.get_rect()
                text3rect.center = (self.center[0] + (self.line/4*2), self.center[1] -100)



                self.screen.blit(text, textrect)
                self.screen.blit(text2, textrect2)
                self.screen.blit(text3, text3rect)

    def get_speed(self):
        return self.set_speed