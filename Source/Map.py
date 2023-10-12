import random



class Level1:
    def __init__ ( self ) :
        self.M = 10
        self.N = 10
        maping = [0,1]
        self.maze = []
        for i in range(0, self.N):
            for j in range(0, self.M):
                if ((j==0 and i == 1) or (j==self.M-1 and i == self.M-2)):
                    self.maze.append(0)
                elif (i == 0 or i == self.M-1 or j == 0 or j == self.M-1):
                    self.maze.append(1)
                else:
                    self.maze.append(random.choice(maping))
        self.item = []

    def draw(self, display_surf, image_surf, image1_surf):
        
        for i in range(0, self.N):
            for j in range(0, self.M):
                if self.maze[i * self.N + j] == 1:
                    display_surf.blit(image_surf,(j * 60, i * 60))
                else:
                    self.item.append(i * self.N + j)
                    display_surf.blit(image1_surf, (j * 60, i * 60))  

    def draw_item(self, display_surf, question_block):

        real = []

        number = int((self.M*self.N)/100)

        i=1
        while i <= number:
            choice = random.choice(self.item)
            real.append(choice)
            j = int(choice % 10)
            k = int(choice / 10)
            display_surf.blit(question_block,(j*60,k*60))
            i = i+1

      

        return number, real
    
    def maintain_item(self, size, real, display_surf, question_block):

        i=0
        if size > 0 :
            while i < size:
                 j = int(real[i] % 10)
                 k = int(real[i] / 10)
                 display_surf.blit(question_block, (j*60,k*60))
                 i = i+1
            
   
            
        
        

class Level2:
    def __init__ (self) :
        self.M = 15
        self.N = 15
        maping = [0,1]
        self.maze = []
        for i in range(0, self.N):
            for j in range(0, self.M):
                if ((j==0 and i == 1) or (j==self.M-1 and i == self.M-2)):
                    self.maze.append(0)
                elif (i == 0 or i == self.M-1 or j == 0 or j == self.M-1):
                    self.maze.append(1)
                else:
                    self.maze.append(random.choice(maping))
        self.item = []

    def draw(self, display_surf, image_surf, image1_surf):
        for i in range(0, self.N):
            for j in range(0, self.M):
                if self.maze[i * self.N + j] == 1:
                    display_surf.blit(image_surf,(j * 40, i * 40))
                else:
                    self.item.append(i * self.N + j)
                    display_surf.blit(image1_surf, (j * 40, i * 40))

    def draw_item(self, display_surf, question_block):

        real = []

        number = int((self.M*self.N)/100)

        i=1
        while i <= number:
            choice = random.choice(self.item)
            real.append(choice)
            j = int(choice % 15)
            k = int(choice / 15)
            display_surf.blit(question_block,(j*40,k*40))
            i = i+1

      

        return number, real
    
    def maintain_item(self, size, real, display_surf, question_block):

        i=0
        while i < size:
            j = int(real[i] % 15)
            k = int(real[i] / 15)
            display_surf.blit(question_block, (j*40,k*40))
            i = i+1

class Level3:
    def __init__(self) :
        self.M = 20
        self.N = 20
        maping = [0,1]
        self.maze = []
        for i in range(0, self.N):
            for j in range(0, self.M):
                if ((j==0 and i == 1) or (j==self.M-1 and i == self.M-2)):
                    self.maze.append(0)
                elif (i == 0 or i == self.M-1 or j == 0 or j == self.M-1):
                    self.maze.append(1)
                else:
                    self.maze.append(random.choice(maping))
        self.item = []

    def draw(self, display_surf, image_surf, image1_surf):
       for i in range(0, self.N):
            for j in range(0, self.M):
                if self.maze[i * self.N + j] == 1:
                    display_surf.blit(image_surf,(j * 30, i * 30))
                else:
                    self.item.append(i * self.N + j)
                    display_surf.blit(image1_surf, (j * 30, i * 30))

    def draw_item(self, display_surf, question_block):

        real = []

        number = int((self.M*self.N)/100)

        i=1
        while i <= number:
            choice = random.choice(self.item)
            real.append(choice)
            j = int(choice % 20)
            k = int(choice / 20)
            display_surf.blit(question_block,(j*30,k*30))
            i = i+1

      

        return number, real

    def maintain_item(self, size, real, display_surf, question_block):

        i=0
        while i < size:
            j = int(real[i] % 20)
            k = int(real[i] / 20)
            display_surf.blit(question_block, (j*30,k*30))
            i = i+1

class Level4:
    def __init__(self):
        self.M = 25
        self.N = 25
        maping = [0,1]
        self.maze = []
        for i in range(0, self.N):
            for j in range(0, self.M):
                if ((j==0 and i == 1) or (j==self.M-1 and i == self.M-2)):
                    self.maze.append(0)
                elif (i == 0 or i == self.M-1 or j == 0 or j == self.M-1):
                    self.maze.append(1)
                else:
                    self.maze.append(random.choice(maping))
        self.item = []


    def draw(self, display_surf, image_surf, image1_surf):
        for i in range(0, self.N):
            for j in range(0, self.M):
                if self.maze[i * self.N + j] == 1:
                    display_surf.blit(image_surf,(j * 24, i * 24))
                else:
                    self.item.append(i * self.N + j)
                    display_surf.blit(image1_surf, (j * 24, i * 24))

    def draw_item(self, display_surf, question_block):

        real = []

        number = int((self.M*self.N)/100)

        i=1
        while i <= number:
            choice = random.choice(self.item)
            real.append(choice)
            j = int(choice % 25)
            k = int(choice / 25)
            display_surf.blit(question_block,(j*24,k*24))
            i = i+1

      

        return number, real

    def maintain_item(self, size, real, display_surf, question_block):

        i=0
        while i < size:
            j = int(real[i] % 25)
            k = int(real[i] / 25)
            display_surf.blit(question_block, (j*24,k*24))
            i = i+1
            
               
class Level5:
    def __init__(self):
        self.M = 30
        self.N = 30
        maping = [0,1]
        self.maze = []
        for i in range(0, self.N):
            for j in range(0, self.M):
                if ((j==0 and i == 1) or (j==self.M-1 and i == self.M-2)):
                    self.maze.append(0)
                elif (i == 0 or i == self.M-1 or j == 0 or j == self.M-1):
                    self.maze.append(1)
                else:
                    self.maze.append(random.choice(maping))
        self.item = []


    def draw(self, display_surf, image_surf, image1_surf):
        for i in range(0, self.N):
            for j in range(0, self.M):
                if self.maze[i * self.N + j] == 1:
                    display_surf.blit(image_surf,(j * 20, i * 20))
                else:
                    self.item.append(i * self.N + j)
                    display_surf.blit(image1_surf, (j * 20, i * 20))

    def draw_item(self, display_surf, question_block):

        real = []

        number = int((self.M*self.N)/100)

        i=1
        while i <= number:
            choice = random.choice(self.item)
            real.append(choice)
            j = int(choice % 30)
            k = int(choice / 30)
            display_surf.blit(question_block,(j*20,k*20))
            i = i+1

      

        return number, real

    def maintain_item(self, size, real, display_surf, question_block):

        i=0
        while i < size:
            j = int(real[i] % 30)
            k = int(real[i] / 30)
            display_surf.blit(question_block, (j*20,k*20))
            i = i+1
