from pygame import *
from numpy import zeros,array
from random import randint
init()
res=[700,700]
window=display.set_mode(res)
clock = time.Clock()
black=(0,0,0)
white=(255,255,255)
blue=(0,0,255)
green=(0,255,0)
grey = (100,100,100)
darkgrey = (20,20,20)


class Game(object):
    def __init__(self,num):
        self.win = False
        file = open("table"+str(num)+".dat")
        self.sol = []
        for line in file:
            tmp = []
            for char in line:
                if char in ["0","1"]:
                    tmp.append(int(char))
            self.sol.append(tmp)
        self.tab = zeros((len(self.sol[0]),len(self.sol)))
        self.size = (res[0]-200)/max(len(self.tab),len(self.tab[0]))
        self.tx = []
        for i in range(len(self.sol)):      
            tmp = []
            counter = 0
            for j in range(len(self.sol[i])):
                if self.sol[i][j]==0:
                    if counter > 0:
                        tmp.append(counter)
                    counter = 0
                    continue
                if self.sol[i][j]==1:
                    counter = counter + 1
            if counter > 0:
                tmp.append(counter)
            self.tx.append(tmp)
        self.ty = []
        for i in range(len(self.sol[0])):      
            tmp = []
            counter = 0
            for j in range(len(self.sol)):
                if self.sol[j][i]==0:
                    if counter > 0:
                        tmp.append(counter)
                    counter = 0
                    continue
                if self.sol[j][i]==1:
                    counter = counter + 1
            if counter > 0:
                tmp.append(counter)
            self.ty.append(tmp)
        self.Font=font.SysFont("Arial",self.size/2)


    def draw(self):
        window.fill(black)
        if not self.win:
            for i in range(len(self.tab)):
                for j in range(len(self.tab[0])):
                    if self.tab[i][j]==0:
                        draw.rect(window,grey,Rect(200+self.size*i,200+self.size*j,self.size-1,self.size-1),0)
                    elif self.tab[i][j]==-1:
                        draw.rect(window,darkgrey,Rect(200+self.size*i,200+self.size*j,self.size-1,self.size-1),0)
                    elif self.tab[i][j]==1:
                        draw.rect(window,blue,Rect(200+self.size*i,200+self.size*j,self.size-1,self.size-1),0)
            for i in range(len(self.tx)):
                for j in range(len(self.tx[i])):
                    text = self.Font.render(str(self.tx[i][j]),True,white)
                    window.blit(text,(200+i*self.size+self.size*0.4,190-(len(self.tx[i])-j)*self.size/2))  
            for i in range(len(self.ty)):
                for j in range(len(self.ty[i])):
                    text = self.Font.render(str(self.ty[i][j]),True,white)
                    window.blit(text,(190-(len(self.ty[i])-j)*self.size/2,200+i*self.size+self.size*0.4))
        if self.win:
            for i in range(len(self.tab)):
                for j in range(len(self.tab[0])):
                    if self.tab[i][j]==1:
                        draw.rect(window,blue,Rect(200+self.size*i,200+self.size*j,self.size,self.size),0)
            for i in range(len(self.tx)):
                for j in range(len(self.tx[i])):
                    text = self.Font.render(str(self.tx[i][j]),True,white)
                    window.blit(text,(200+i*self.size+self.size*0.4,190-(len(self.tx[i])-j)*self.size/2))  
            for i in range(len(self.ty)):
                for j in range(len(self.ty[i])):
                    text = self.Font.render(str(self.ty[i][j]),True,white)
                    window.blit(text,(190-(len(self.ty[i])-j)*self.size/2,200+i*self.size+self.size*0.4))
            Font=font.SysFont("Arial",80)
            text = Font.render("YOU WIN",True,white)
            window.blit(text,(250,300))      
        Font2=font.SysFont("Arial",20)
        window.blit(Font2.render("r - reset level",True,white),(10,20))      
        window.blit(Font2.render("> - next level",True,white),(10,45))  
        window.blit(Font2.render("< - previous level",True,white),(10,70))   
    
    def event(self):
        if 200 < mouse.get_pos()[0] < res[0]-10 and 200 < mouse.get_pos()[1] < res[1]-10:
            i = (mouse.get_pos()[0]-200)/self.size
            j = (mouse.get_pos()[1]-200)/self.size
            if mouse.get_pressed()[0]:
                self.tab[i][j] = 1
            elif mouse.get_pressed()[1]:
                self.tab[i][j] = 0
            elif mouse.get_pressed()[2]:
                self.tab[i][j] = -1
    
    def check(self):
        result = True
        for i in range(len(self.sol[0])):
            for j in range(len(self.sol)):
                if self.sol[i][j] == 0 and self.tab[i][j] == 1:
                    result = False
                if self.sol[i][j] == 1 and self.tab[i][j] in [0,-1]:
                    result = False
        self.win = result

    def solver(self):
        def heur1():
            for i in range(len(self.tab)):
                if len(self.tx[i])==1:
                    if self.tx[i][0]>len(self.tab)/2:
                        for j in range((len(self.tab)-self.tx[i][0]),self.tx[i][0]):
                            self.tab[i][j] = 1
            for i in range(len(self.tab)):
                if len(self.ty[i])==1:
                    if self.ty[i][0]>len(self.tab)/2:
                        for j in range((len(self.tab)-self.ty[i][0]),self.ty[i][0]):
                            self.tab[j][i] = 1
        def heur2():
            for i in range(len(self.tab)):
                if len(self.tx[i])==0:
                    for j in range(len(self.tab[0])):
                        self.tab[i][j] = -1
            for i in range(len(self.tab[0])):
                if len(self.ty[i])==0:
                    for j in range(len(self.tab)):
                        self.tab[j][i] = -1                       
        def heur3():

            for l in range(len(self.tab)):
                suma = sum(self.tx[l])
                votes = zeros(len(self.tab))
                all = 0
                for k in range(20000):
                    tmp = zeros(len(self.tab))
                    for i in range(suma):
                        r = randint(0,len(self.tab)-1)
                        while tmp[r]==1:
                            r = randint(0,len(self.tab)-1)
                        tmp[r]=1            
                    test = []
                    counter = 0
                    for j in range(len(self.sol[i])):
                        if tmp[j]==0:
                            if counter > 0:
                                test.append(counter)
                            counter = 0
                            continue
                        if tmp[j]==1:
                            counter = counter + 1
                    if counter > 0:
                        test.append(counter)
                    #print test
                    #print tmp
                    if test==self.tx[l]:
                        all = all + 1
                        votes = votes + tmp
                print votes
                print all
                for i in range(len(votes)):
                    if votes[i]==all and all>10:
                        self.tab[l][i] = 1

            for l in range(len(self.tab[0])):
                suma = sum(self.ty[l])
                votes = zeros(len(self.tab[0]))
                all = 0
                for k in range(20000):
                    tmp = zeros(len(self.tab[0]))
                    for i in range(suma):
                        r = randint(0,len(self.tab[0])-1)
                        while tmp[r]==1:
                            r = randint(0,len(self.tab[0])-1)
                        tmp[r]=1            
                    test = []
                    counter = 0
                    for j in range(len(self.sol[i])):
                        if tmp[j]==0:
                            if counter > 0:
                                test.append(counter)
                            counter = 0
                            continue
                        if tmp[j]==1:
                            counter = counter + 1
                    if counter > 0:
                        test.append(counter)
                    #print test
                    #print tmp
                    if test==self.ty[l]:
                        all = all + 1
                        votes = votes + tmp
                print votes
                print all
                for i in range(len(votes)):
                    if votes[i]==all and all>10:
                        self.tab[i][l] = 1
        #heur1()
        #heur2()
        heur3()

numgame = 1
maxnumgame = 3
game = Game(numgame)
endgame = False
while not endgame:
	for ev in event.get():
		if ev.type == QUIT:
			endgame = True
        if ev.type == KEYDOWN:
            if ev.key == K_r:
                game = Game(numgame)
            if ev.key == K_RIGHT:
                if numgame < maxnumgame:
                    numgame = numgame + 1
                    game = Game(numgame)
            if ev.key == K_LEFT:
                if numgame > 1:
                    numgame = numgame - 1
                    game = Game(numgame)
            if ev.key == K_s:
                game.solver()

	game.event()
	game.draw()
	game.check()
	clock.tick(15)
	display.flip()
