## 기본적인 미로 참조  https://pythonspot.com/en/maze-in-pygame/
## 파이썬 기술 참조   https://wikidocs.net/book/1
## 배경음악  bgm https://bgmstore.net/


from pygame.locals import *
import pygame
import random
from Map import *  ## 랜덤 맵, 아이템 생성코드위치
from GameStart import * ## 게임첫화면 코드
from GameOver import * ## 시간초과시화면 코드
import time
from Player import *  ## 플레이어(캐릭터위치) 코드
from Clear import *  ## 5단계클리어시화면 코드
from character import * ## 첫화면다음 캐릭터선택창 코드
import sys  
import pygame.mixer
import os
pygame.init()


## 브금이랑 효과음
sound_file = "Asset/Sound/Undertale-Megalovania-Piano-Ver-.wav"
bomb_file = "Asset/Sound/bomb.wav"
urgent_file = "Asset/Sound/HORROR.wav"
mixer = pygame.mixer
mixer.init()



starttime = time.time()


global gametime  ## timer
global number  ## 아이템의 개수

global track  ## BGM
global cnt  ## 맵바꾸기위한 숫자카운트
global char  ## 캐릭터 선택
cnt = -1
itemcnt = 0
charitem = 0
finishtime = 130
skill = 5
char = 0

track = mixer.Sound(sound_file)
urgent = mixer.Sound(urgent_file)
effect = mixer.Sound(bomb_file)

timecnt = 0


if cnt == -1:
   cnt = Game_Start() ##첫화면
   char = character() ##캐릭터선택화면

clock = pygame.time.Clock()

class App:

    ## 화면크기설정
    windowWidth = 700
    windowHeight = 600
    player = 0

    def setname(self, name):
        self.name = name
        
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self._block_surf = None
        ## 클래스로만들어진 미로 맵을 단계별로 불러옴.
        if cnt == 0 :
            self.maze = Level1()
            self.player = Player1()
        elif cnt == 1:
            self.maze = Level2()
            self.player = Player2()
        elif cnt == 2:
            self.maze = Level3()
            self.player = Player3()
        elif cnt == 3:
            self.maze = Level4()
            self.player = Player4()
        elif cnt == 4:
            self.maze = Level5()
            self.player = Player5()


    def on_init(self):
        ## 맵을 만드는데 필요한 벽돌, 땅, 캐릭터, 아이템의 이미지를 가져옴.
        global char
        pygame.init()
        self._display_surf = pygame.display.set_mode((self.windowWidth,self.windowHeight), pygame.HWSURFACE)

        pygame.display.set_caption('Maze Runner')
        self._running = True
        self._block_surf = pygame.image.load("Asset/Graphic/block%d.jpg" %cnt).convert()
        self._ground_surf = pygame.image.load("Asset/Graphic/ground%d.jpg" %cnt).convert()
        if char == 1:
           self._image_surf = pygame.image.load("Asset/Graphic/squ%d.jpg" %cnt).convert()
        elif char == 2:
           self._image_surf = pygame.image.load("Asset/Graphic/fire%d.jpg" %cnt).convert()
        elif char == 3:
           self._image_surf = pygame.image.load("Asset/Graphic/pika%d.jpg" %cnt).convert()
        self._question_surf = pygame.image.load("Asset/Graphic/question%d.jpg" %cnt).convert()

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False

    def on_loop(self):
        pass
   
    def on_render(self):
       ## 화면을 출력하는 부분. 계속해서 반복 실행됨.
       global cnt
       global item
       global t1
       global finishtime
       global itemcnt
       global skill
       global track
       global urgent
       self._display_surf.fill((0,0,0))
       self.maze.draw(self._display_surf, self._block_surf, self._ground_surf)
       if itemcnt == 0 :
          t1 = self.maze.draw_item(self._display_surf, self._question_surf)
          itemcnt = itemcnt + 1
       else:
          self.maze.maintain_item(t1[0],t1[1],self._display_surf,self._question_surf)
             
       self._display_surf.blit(self._image_surf,(self.player.x,self.player.y))
          
       endtime = time.time()
       gametime = str(int(endtime-starttime))
       dan = pygame.font.Font(None, 45)
       le = cnt+1
       dant = "Level"+str(le)
       danx = dan.render((dant), 1, (255,255,255))
       self._display_surf.blit(danx, ( 600,50))
       Limit = pygame.font.Font(None, 50)
       namet = "Limit"
       Limitx = Limit.render((namet), 1, (255,0,0))
       self._display_surf.blit(Limitx, ( 610,150))
       Limittime = pygame.font.Font(None, 50)
       namett = "%d"%finishtime
       Limittimex = Limittime.render((namett), 1, (255,0,0))
       self._display_surf.blit(Limittimex, ( 620,200))
       timer = pygame.font.Font(None, 50)
       name = "Timer"      
       if int(gametime) >= int(finishtime-20) :
          timerx = timer.render((name), 1, (255,0,0))
       else:
          timerx = timer.render((name), 1, (255,255,255))
       self._display_surf.blit(timerx, (600,300))
       font = pygame.font.Font(None, 50)
       if int(gametime) >= int(finishtime-20) :
          text = font.render((gametime), 1, (255,0,0))
       else:
          text = font.render((gametime), 1, (255,255,255))
       self._display_surf.blit(text, (620,350))
       Skills = pygame.font.Font(None, 50)
       Skillt = "Skills"
       Skillst = Skills.render((Skillt), 1, (255,242,0))
       self._display_surf.blit(Skillst, (600,450))
       Skillcnt = pygame.font.Font(None, 50)
       Skillcntt = "%d"%skill
       Skillcnts = Skillcnt.render((Skillcntt), 1, (255,255,255))
       self._display_surf.blit(Skillcnts, (650,500))
       start = pygame.font.Font(None, 25)
       startt = "Start"
       starts = start.render((startt), 1, (255,255,255))
       self._display_surf.blit(starts, (0,self.player.standard))
       finish = pygame.font.Font(None, 25)
       finisht = "Finish"
       finishs = finish.render((finisht), 1, (255,255,255))
       self._display_surf.blit(finishs, ((self.maze.M-1)*self.player.standard,(self.maze.M-2)*self.player.standard))

       if skill == 0 :
          track.stop()
          urgent.play(-1)
       
       if ( int(gametime) == int(finishtime) and skill != 0):
          track.stop()
          cnt = Game_Over()
          self.on_cleanup()
       elif ( int(gametime) == int(finishtime) and skill == 0):
          urgent.stop()
          cnt = Game_Over()
          self.on_cleanup()
             
       pygame.display.flip()
       clock.tick(60)

    def on_cleanup(self):
        pygame.quit()
        sys.exit()
        self._running = False

    def on_execute(self):
        pygame.init()
        global finishtime
        global skill
        if self.on_init() == False: 
            self._running = False


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.on_cleanup()
                break

        while( self._running ):
            time.sleep(0.1) ## 캐릭터의 움직이는 속도를 제어?한다.
            a = self.item1  
            b = self.item2
            item_command = [a,b]  ## 아이템을 랜덤실행시키기위해 리스트에추가.
            pygame.event.pump()
            keys = pygame.key.get_pressed()

            playerxy = int(self.player.x/self.player.standard+self.player.y/self.player.standard*(600/self.player.standard))

            ## 방향키로 움직이게만드는 부분.
            ## 움직일때마다 움직이는 방향의 리스트를 확인하여 0이면 움직이고 그렇지않으면 움직일 수 없다.
            if (keys[K_RIGHT] and self.maze.maze[playerxy+1] == 0):
                self.player.moveRight()
            elif (keys[K_LEFT] and self.maze.maze[playerxy-1] == 0):
                self.player.moveLeft()
            elif (keys[K_UP] and self.maze.maze[playerxy-int(600/self.player.standard)] == 0):
                self.player.moveUp()
            elif (keys[K_DOWN] and self.maze.maze[playerxy+int(600/self.player.standard)] == 0):
                self.player.moveDown()

            ## 스킬을 사용하는 부분
            if keys[K_SPACE]:
               if (keys[K_RIGHT] and self.maze.maze[playerxy+1] == 1):
                  if skill != 0:
                     skill = self.skilluse(playerxy+1, skill)
               elif (keys[K_LEFT] and self.maze.maze[playerxy-1] == 1):
                  if skill != 0:
                     skill = self.skilluse(playerxy-1, skill)
               elif (keys[K_UP] and self.maze.maze[playerxy-int(600/self.player.standard)] == 1):
                  if skill != 0:
                     skill = self.skilluse(playerxy-int(600/self.player.standard), skill)
               elif (keys[K_DOWN] and self.maze.maze[playerxy+int(600/self.player.standard)] == 1):
                  if skill != 0:
                     skill = self.skilluse(playerxy+int(600/self.player.standard), skill)

            self.on_loop()
            self.on_render()

            global t1
            number = t1[0]
            item = t1[1] 
            i=0
            global charitem

            ## 캐릭터에 의해 사용된 아이템처리 부분
            if number > 0:
               while i < number:
                  if playerxy == item[i]:
                        command = random.choice(item_command)
                        itemuse = command(finishtime, skill)
                        skill = itemuse[1]
                        finishtime = itemuse[0]
                        item[i] = 5000
                        
                        
                        
                  i = i +1
            
            ## 미로의 클리어 조건과, 다음 미로를 위한 초기화부분
            if (int(self.player.x/self.player.standard+self.player.y/self.player.standard*(600/self.player.standard)) == int((self.maze.M-1)+(self.maze.N-2)*(600/self.player.standard))):
                global cnt
                global track
                global itemcnt
                cnt = cnt + 1
                itemcnt = 0
                charitem = 0
                
                if cnt == 5:
                   track.stop()
                   cnt = Game_Clear()
                   self.on_cleanup()
                   
                   
                if cnt != 5 and __name__ == "__main__":
                    pygame.init()
                    Game = App()
                    Game.on_execute()

    ## 아이템및 사용 함수                
    def item1(self, gametime, skill):
      return int(gametime + 10), int(skill+3)
    def item2(self, gametime, skill):
      return int(gametime - 10), int(skill+3)
    def skilluse(self, afterposition, skill):
       global effect
       del self.maze.maze[afterposition]
       self.maze.maze.insert(afterposition,0)
       effect.play(1)
       
       
       return int(skill-1)
       
       

        


if cnt == 0 :
    if __name__ == "__main__" :
        track.play(loops=-1)
        pygame.init()
        theApp = App()
        theApp.on_execute()


            
        
   
