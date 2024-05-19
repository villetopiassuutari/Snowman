import pygame
pygame.init()

def alusta():
    #Alustaa pygame ikkunan ja palauttaa näyttöolion
    pygame.init()
    naytto = pygame.display.set_mode((640, 480))
    return naytto

naytto = alusta()
pygame.display.set_caption("Lumiukko liikkuu")


#Pallojen aloituskoordinaatit
x1 = 320
y1 = 420

x2 = 320
y2 = 320

x3 = 320
y3 = 260




#Lumiukon nopeus
vel = 10

#Ohjelma käynnissä
run = True

while run:
    #Luo viiveen 10ms
    pygame.time.delay(10)


# Pygamen pääsilmukka, jossa odotetaan ikkunan sulkeutumista
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


#Lumiukon ohjaaminen
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x1 -= vel
        x2 -= vel
        x3 -= vel
    if keys[pygame.K_RIGHT]:
        x1 += vel
        x2 += vel
        x3 += vel
    if keys[pygame.K_UP]:
        y1 -= vel
        y2 -= vel
        y3 -= vel
    if keys[pygame.K_DOWN]:
        y1 += vel
        y2 += vel
        y3 += vel

    #Tekee taustasta mustan ja estää sen, että lumiukko ei "jää" aina edelliseen sijaintiinsa
    naytto.fill((0, 0, 0))

    #Piirretään pallot näytölle
    pygame.draw.circle(naytto, (255, 255, 255), (x1, y1), 60, 60)
    pygame.draw.circle(naytto, (255, 255, 255), (x2, y2), 40, 40)
    pygame.draw.circle(naytto, (255, 255, 255), (x3, y3), 20, 20)
    

    #Päivittää näytön
    pygame.display.update()


pygame.quit()
    