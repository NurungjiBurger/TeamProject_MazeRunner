import pygame
pygame.init()

def character():
    global char
    pygame.init()
    ourscreen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Maze Runner")
    finish = False
    
    background = pygame.image.load("character.jpg")

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True



            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_LEFT]:
                char = 1
                finish = True
            elif pressed[pygame.K_DOWN]:
                char = 2
                finish = True
            elif pressed[pygame.K_RIGHT]:
                char = 3
                finish = True


            ourscreen.fill((0,0,0))

        ourscreen.blit(background, (0,0))
        notice = pygame.font.Font(None, 40)
        noticet = "Select your character for Direction key"
        notices = notice.render((noticet),1,(0,0,0))
        ourscreen.blit(notices, (30,100))
        pygame.display.flip()


    return char

                
