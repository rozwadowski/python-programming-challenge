from pygame import *
import numpy as np
from time import sleep


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
        self.newgame = False

        self.winMatrix = [[False, True, False, False, True],
                          [False, False, True, True, False],
                          [True, False, False, False, True],
                          [True, False, True, False, False],
                          [False, True, False, True, False]]
        self.buttons = [oButton(0, 430, 120, 120, "rock.png"),
                        oButton(1, 150, 270, 120, "paper.png"),
                        oButton(2, 710, 270, 120, "scissors.png"),
                        oButton(3, 280, 540, 120, "lizard.png"),
                        oButton(4, 580, 540, 120, "spock.png")]

        self.turn = "One"
        self.p1 = -1
        self.p2 = -1
        self.winner = ""

    def event(self):
        for button in self.buttons:
            button.event(self)
        if self.turn == "Results":
            if self.p1 == self.p2:
                self.winner = "Draw"
            else:
                if not self.winMatrix[self.p1][self.p2]:
                    self.winner = "Player one"
                else:
                    self.winner = "Player two"

    def draw(self):
        self.window.fill((0, 0, 0))
        for button in self.buttons:
            button.draw(self)

        if self.turn == "One":
            text = self.Font.render("Player one", True, (255, 255, 255))
            self.window.blit(text, (370, 340))
        elif self.turn == "Two":
            text = self.Font.render("Player two", True, (255, 255, 255))
            self.window.blit(text, (370, 340))
        elif self.turn == "Results":
            if self.winner == "Draw":
                text = self.Font.render("Draw", True, (255, 255, 255))
                self.window.blit(text, (400, 340))
                draw.circle(self.window, (255, 0, 0),
                            (self.buttons[self.p1].x, self.buttons[self.p1].y),
                            120, 3)
            else:
                text = self.Font.render("The winner: "+self.winner,
                                        True, (255, 255, 255))
                draw.circle(self.window, (255, 0, 255),
                            (self.buttons[self.p1].x,
                             self.buttons[self.p1].y), 120, 3)
                draw.circle(self.window, (255, 255, 0),
                            (self.buttons[self.p2].x,
                             self.buttons[self.p2].y), 120, 3)
                self.window.blit(text, (350, 340))
                self.newgame = True


def main():
    init()
    game = Game()

    while not game.endgame:
        for ev in event.get():
            if ev.type == QUIT:
                game.endgame = True

        if game.newgame:
            sleep(3)
            game = Game()
        game.draw()
        game.event()

        game.clock.tick(20)
        display.flip()


if __name__ == "__main__":
    main()
