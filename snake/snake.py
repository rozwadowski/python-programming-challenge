from pygame import *
import numpy as np
from time import sleep
from random import randint


class oButton(object):
    def __init__(self, num, x, y, r, text=""):
        self.num = num
        self.x = x
        self.y = y
        self.r = r
        self.im = image.load(text)
        self.im = transform.scale(self.im, (200, 200))

    def click(self):
        if mouse.get_pressed()[0]:
            if np.sqrt((mouse.get_pos()[0]-self.x)**2
                       + (mouse.get_pos()[1]-self.y)**2) <= self.r:
                return True
        return False

    def event(self, game):
        if self.click() and game.turn == "One":
            game.turn = "Two"
            game.p1 = self.num
            sleep(1)
        elif self.click() and game.turn == "Two":
            game.turn = "Results"
            game.p2 = self.num
            sleep(1)

    def draw(self, game):
        if np.sqrt((mouse.get_pos()[0]-self.x)**2
                   + (mouse.get_pos()[1]-self.y)**2) <= self.r:
            draw.circle(game.window, (0, 255, 0), (self.x, self.y), self.r, 1)
        else:
            draw.circle(game.window, (255, 255, 255),
                        (self.x, self.y), self.r, 1)

        game.window.blit(self.im, (self.x-100, self.y-100))


class Game(object):
    def __init__(self):
        self.res = [860, 680]
        self.window = display.set_mode(self.res)
        self.clock = time.Clock()
        self.Font = font.SysFont("arial", 20)
        self.endgame = False
        self.gameover = False
        self.X = 33
        self.Y = 25
        self.size = 25
        self.snake = [[7, 5], [6, 5], [5, 5]]
        self.dir = [1, 0]
        x = randint(0, self.X-1)
        y = randint(0, self.Y-1)
        while [x, y] in self.snake:
            x = randint(0, self.X-1)
            y = randint(0, self.Y-1)
        self.apple = [x, y]
        self.points = 0

    def move(self, x):
        if self.dir == [0, 1]:
            self.dir = [-x, 0]
        elif self.dir == [0, -1]:
            self.dir = [x, 0]
        elif self.dir == [1, 0]:
            self.dir = [0, x]
        elif self.dir == [-1, 0]:
            self.dir = [0, -x]

    def event(self):
        if not self.gameover:
            if not (self.snake[0][0]+self.dir[0] == self.apple[0]
                    and self.snake[0][1]+self.dir[1] == self.apple[1]):
                for i in range(len(self.snake)-1, 0, -1):
                    self.snake[i][0] = self.snake[i-1][0]
                    self.snake[i][1] = self.snake[i-1][1]
                self.snake[0][0] = self.snake[0][0] + self.dir[0]
                self.snake[0][1] = self.snake[0][1] + self.dir[1]
            else:
                self.snake.insert(0, [self.snake[0][0]+self.dir[0],
                                      self.snake[0][1]+self.dir[1]])
                self.points = self.points + 1
                x = randint(0, self.X-1)
                y = randint(0, self.Y-1)
                while [x, y] in self.snake:
                    x = randint(0, self.X-1)
                    y = randint(0, self.Y-1)
                self.apple = [x, y]

            for i in range(1, len(self.snake)):
                if self.snake[i][0] == self.snake[0][0]
                and self.snake[i][1] == self.snake[0][1]:
                    self.gameover = True
            if self.snake[0][0] < 0 or self.snake[0][0] >= self.X
            or self.snake[0][1] < 0 or self.snake[0][1] >= self.Y:
                self.gameover = True

    def draw(self):
        self.window.fill((0, 0, 0))
        for i in range(self.X):
            for j in range(self.Y):
                draw.rect(self.window, (20, 20, 20),
                          Rect(i*self.size, j*self.size,
                               self.size-2, self.size-1), 0)
        for s in self.snake:
            draw.rect(self.window, (20, 255, 20),
                      Rect(s[0]*self.size, s[1]*self.size,
                           self.size-2, self.size-1), 0)
        draw.rect(self.window, (255, 20, 20),
                  Rect(self.apple[0]*self.size, self.apple[1]*self.size,
                       self.size-2, self.size-1), 0)

        text = self.Font.render("Points: "+str(self.points),
                                True, (255, 255, 255))
        self.window.blit(text, (50, 630))
        if self.gameover:
            text = self.Font.render("GAME OVER. Press n to start new game",
                                    True, (255, 255, 255))
            self.window.blit(text, (260, 330))


def main():
    init()
    game = Game()

    while not game.endgame:
        for ev in event.get():
            if ev.type == QUIT:
                game.endgame = True
            if ev.type == KEYDOWN:
                if ev.key == K_LEFT:
                    game.move(-1)
                if ev.key == K_RIGHT:
                    game.move(1)
                if ev.key == K_n:
                    game = Game()
        game.draw()
        game.event()

        game.clock.tick(8)
        display.flip()


if __name__ == "__main__":
    main()
