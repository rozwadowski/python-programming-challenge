# -*- coding: utf-8 -*-

import os
from pygame import *
from time import sleep

init()
res = [800, 640]
window = display.set_mode(res)
clock = time.Clock()
Font = font.SysFont("Arial", 12)


class Browser(object):
    def __init__(self):
        self.path = "."
        self.list = self.sortlist(os.listdir(self.path))
        self.ind = 0
        self.shift = 0
        self.size = 16

    def sortlist(self, listtosort):
        filelist = []
        dirlist = []
        for el in listtosort:
            if os.path.isdir(self.path + "/" + el):
                dirlist.append(el)
            elif os.path.isfile(self.path + "/" + el):
                filelist.append(el)
        return sorted(dirlist) + sorted(filelist)

    def screendraw(self):
        window.fill((0, 0, 0))
        for el in self.list:
                if os.path.isdir(self.path + "/" + el):
                    text = Font.render(el[:25], True, (0, 0, 255))
                    window.blit(text,
                                (20, self.size*(self.list.index(el)
                                                + 1-self.shift)))
                if os.path.isfile(self.path + "/" + el):
                    text = Font.render(el[:25], True, (0, 255, 0))
                    window.blit(text, (20, self.size*(self.list.index(el)
                                                      + 1-self.shift)))
        text = Font.render("<----", True, (0, 0, 255))
        window.blit(text, (20, 0))
        draw.rect(window, (106, 106, 106),
                  Rect(20, self.ind*self.size, 200, self.size), 1)

    def down(self):
        if self.ind < len(self.list):
            if self.ind < 39:
                self.ind = self.ind + 1
            elif self.shift + self.ind < len(self.list):
                self.shift = self.shift + 1

    def up(self):
        if self.shift > 0:
            self.shift = self.shift - 1
        elif self.ind > 0:
            self.ind = self.ind - 1

    def enter(self):
        picked = self.ind + self.shift
        if picked == 0:
            self.path = self.path + "/.."
            self.list = self.sortlist(os.listdir(self.path))
            sleep(0.2)
        elif os.path.isdir(self.path + "/" + self.list[picked-1]):
            self.path = self.path + "/" + self.list[picked-1]
            self.list = self.sortlist(os.listdir(self.path))
            self.ind = 0
            self.shift = 0
            sleep(0.2)
        elif self.list[picked-1][-4:] == ".mp3":
            mixer.music.stop()
            mixer.music.load(self.path + "/" + self.list[picked-1])
            mixer.music.play(1)

    def event(self):
        if 20 < mouse.get_pos()[0] < 220:
            if int(mouse.get_pos()[1]/self.size) < len(self.list):
                self.ind = int(mouse.get_pos()[1]/self.size)

        picked = self.ind + self.shift
        if picked > 0:
            if self.list[picked-1][-4:] in [".jpg", ".png"]:
                photo = image.load(self.path + "/" + self.list[picked-1])
                if photo.get_width() > res[0] - 200:
                    scale = photo.get_width()/(res[0]-200)
                    photo = transform.scale(photo, (res[0]-200,
                                                    scale*photo.get_height()))
                if photo.get_height() > res[1]:
                    scale = photo.get_height()/(res[1])
                    photo = transform.scale(photo,
                                            (photo.get_width(),
                                             res[1]*scale))

                window.blit(photo, (200, 0))
                display.flip()


end = False
browser = Browser()
while not end:
    for ev in event.get():
        if ev.type == QUIT:
            end = True
        if ev.type == KEYDOWN:
            if ev.key == K_DOWN:
                browser.down()
            if ev.key == K_UP:
                browser.up()
            if ev.key == K_RETURN or ev.key == K_KP_ENTER:
                browser.enter()
        if ev.type == MOUSEBUTTONDOWN:
            if ev.button == 1:
                browser.enter()
        if ev.type == MOUSEBUTTONUP:
            if ev.button == 4:
                browser.up()
            elif ev.button == 5:
                browser.down()

    browser.screendraw()
    browser.event()
    clock.tick(15)
    display.flip()
