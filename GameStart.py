import pygame
pygame.init()




def Game_Start():
    pygame.init()
    ourscreen = pygame.display.set_mode((600,600))
    pygame.display.set_caption("Maze Runner")
    finish = False

    background = pygame.image.load("firstscreen.jpg")
    

    while not finish:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finish = True

            

            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_SPACE]:
    
                global cnt
                cnt = 0
                finish = True
                
            ourscreen.fill((0,0,0))
        
        ourscreen.blit(background, (0,0))
        Skills = pygame.font.Font(None, 40)
        Skillt = "Space + Direction Key = Destroy the wall"
        Skillst = Skills.render((Skillt), 1, (255,255,255))
        ourscreen.blit(Skillst, (30,200))
        pygame.display.flip()

    return cnt
        
