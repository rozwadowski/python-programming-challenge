from pygame import *

class Game(object):
    def __init__(self):
        self.tab = [[" "," "," "],[" "," "," "],[" "," "," "]]
        self.Font=font.SysFont("arial",80)
        self.turn = "o"
        self.winner = ""

    def draw(self,window):
        window.fill((0,0,0))
        for i in range(3):
            for j in range(3):
                if self.tab[i][j]==" ":
                    draw.rect(window,(192,192,192),Rect(i*150,j*150,149,149),0)
                elif self.tab[i][j]=="x":
                    draw.rect(window,(0,255,0),Rect(i*150,j*150,149,149),0)
                elif self.tab[i][j]=="o":
                    draw.rect(window,(0,0,255),Rect(i*150,j*150,149,149),0)
                text = self.Font.render(self.tab[i][j],True,(255,255,255))
                window.blit(text,(i*150+55,j*150+25))
        if self.winner != "":
            Font=font.SysFont("arial",24)
            text = Font.render("The winner is <"+self.winner+">. Press n to restart game",True,(0,0,0))
            window.blit(text,(0,160))
    def event(self):
        if mouse.get_pressed()[0]:
            for i in range(3):
                for j in range(3):
                    if mouse.get_pos()[0]>150*i and mouse.get_pos()[0]<150*i+149 and mouse.get_pos()[1]>150*j and mouse.get_pos()[1]<150*j+149:
                        if self.tab[i][j]==" ":
                            self.tab[i][j]=self.turn
                            if self.turn=="o":
                                self.turn="x"
                            elif self.turn=="x":
                                self.turn="o"
    def check(self):
        for i in range(3):
            if self.tab[i][0]==self.tab[i][1] and self.tab[i][1]==self.tab[i][2] and self.tab[i][0]!=" ":
                self.winner = self.tab[i][0]
            if self.tab[0][i]==self.tab[1][i] and self.tab[1][i]==self.tab[2][i] and self.tab[0][i]!=" ":
                self.winner = self.tab[0][i]    
        if self.tab[0][0]==self.tab[1][1] and self.tab[1][1]==self.tab[2][2] and self.tab[0][0]!=" ":
                self.winner = self.tab[0][0]         
        if self.tab[0][2]==self.tab[1][1] and self.tab[1][1]==self.tab[2][0] and self.tab[0][2]!=" ":
                self.winner = self.tab[0][2]     
            
def main():
    init()
    window=display.set_mode((450,450))
    clock = time.Clock()

    end = False
    game = Game()
    while not end:
        for ev in event.get():
            if ev.type == QUIT:
                end=True
            if ev.type == KEYDOWN:
                if ev.key == K_n:
                    game=Game()

        
        game.draw(window)
        game.event()
        game.check()
        clock.tick(20)
        display.flip()

if __name__=="__main__":
    main()