import pygame
pygame.init()

def Game_Clear():
    pygame.init()
    ourscreen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Maze Runner")
    finish = False

    background = pygame.image.load("Clear.jpg")

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
    
                global cnt
                cnt = 5
                finish = True
                
            ourscreen.fill((0,0,0))
        
        ourscreen.blit(background, (0,0))
        pygame.display.flip()

    
    return cnt
    
