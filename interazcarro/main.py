import pygame
import modelo1
import modelo2
import serial
import asyncio
import serial.tools.list_ports

orange = '#dc4e0c'
blue = '#061a2a'
white = (244, 245, 247)
gold = (215, 166, 75)
red = (199, 33, 56)
defaul_color = white

ports = serial.tools.list_ports.comports()
puerto =0
for port, desc, hwid in sorted(ports):
    puerto = port
    break
print(puerto)
ser = serial.Serial(
    port=puerto, baudrate=115200,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,timeout=10
)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 480))
    pygame.display.set_caption("velocimetro")
    derecha = modelo1.Tablero(screen, default_color=defaul_color)

    ind = modelo2.indice(screen, default_color=defaul_color)

    # se pone el fondo azul

    background = pygame.Surface(screen.get_size())
    background.fill(pygame.Color(blue))

    clock = pygame.time.Clock()
    hight = derecha.hight
    vel = 0
    running = True
    arriba = False
    pos = 0
    ser.flush()
    peda = 0

    while running:
        time_delta = clock.tick(60)/1000.0
        try:
            a = ser.readline()
            peda = (int(str(a)[2:-5]) - 1020) / 2200
            peda = peda * 100
        except:
            peda =0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                selected = ind.getsimbol(pos)
                if selected <= 3:
                    a = ind.animar(selected)
                    if  a == 3:
                        derecha.default_color = orange
                    elif a == 1:
                        derecha.default_color = gold
                    else:
                        derecha.default_color =white
                elif selected >=7:
                    ser.write(str(selected).encode())


                print(selected)


        derecha.sethight(hight)
        screen.blit(background, (0, 0))
        if vel < 100 and arriba == False:
            vel +=.1
        else:
            arriba = True

        if vel > 0 and arriba == True:
            vel -=.1
        else:
            arriba = False

        derecha.vel = vel

        derecha.dibujarvel()
        derecha.dibujarpedal(peda)

        ind.dibujar()

        pygame.display.update()


    pygame.quit()
main()
