from pygame import *
from random import randint,choice
from time import sleep
import numpy as np
from igraph import *

class Maze(object):
	def __init__(self):
		self.res=[680,680]
		self.window=display.set_mode(self.res)
		self.clock = time.Clock()
		self.Font=font.SysFont("arial",20)
		self.stack = []
		self.vis = []
	
		# creating grid
		N = 30
		g = Graph()
		g.add_vertices(N*N)	# wierzcholkibara

		for i in range(N):	# krawedzie
			for j in range(N-1):
				g.add_edges([(i*N+j,i*N+j+1)])

		for i in range(N-1):	# krawedzie
			for j in range(N):
				g.add_edges([(i*N+j,(i+1)*N+j)])
		# creating maze - Randomized Prim's Algorithm
		Cells = [0]
		Frontier = [1,N]
		while len(Frontier)>0:
			cF = choice(Frontier)
			a = []
			for i in range(g.degree()[cF]):
				a.append(g.vs[cF].neighbors()[i].index)
			cl = choice(a)
			while not cl in Cells:
				cl = choice(a)
			Cells.append(cF)
			for i in range(g.degree()[cF]):
				if not g.vs[cF].neighbors()[i].index in Cells and not g.vs[cF].neighbors()[i].index in Frontier:
					Frontier.append(g.vs[cF].neighbors()[i].index)
			g.delete_edges((cl,cF))
			Frontier.remove(cF)
		
		# plotting maze
		draw.rect(self.window,(255,255,255),Rect(50-10,50-10,N*20,N*20),1)
		for i in g.es:
			x1 = i.tuple[0]%N
			y1 = i.tuple[0]/N
			x2 = i.tuple[1]%N
			y2 = i.tuple[1]/N
			if y1 == y2:
				draw.line(self.window,(255,255,255),((x1+x2)/2*20+10+50,y1*20-10+50),((x1+x2)/2*20+10+50,y1*20+10+50),1)
			if x1 == x2:
				draw.line(self.window,(255,255,255),(x1*20-10+50,(y1+y2)/2*20+10+50),(x1*20+10+50,(y1+y2)/2*20+10+50),1)
		
		draw.rect(self.window,(0,255,0),Rect(45,45,10,10),0)
		draw.rect(self.window,(0,0,255),Rect(45+20*(N-1),45+20*(N-1),10,10),0)
		
		# maze: empty walls are edges
		self.g2 = Graph()
		self.g2.add_vertices(N*N)	# wierzcholkibara

		for i in range(N):	# krawedzie
			for j in range(N-1):
				if not  g.are_connected(i*N+j, i*N+j+1):
					self.g2.add_edges([(i*N+j,i*N+j+1)])
		
		
		for i in range(N-1):	# krawedzie
			for j in range(N):
				if not  g.are_connected(i*N+j, (i+1)*N+j):
					self.g2.add_edges([(i*N+j,(i+1)*N+j)])			
		# finding path 0->N
		self.search_path(0,N*N-1)
		# print path N->0
		visitor = self.vis[-1]
		visitor2 = self.vis[-2]
		x1 = visitor%N
		y1 = visitor/N
		x2 = visitor2%N
		y2 = visitor2/N
		draw.line(self.window,(255,165,0),(x1*20+50,y1*20+50),(x2*20+50,y2*20+50),1)
		i = len(self.vis)-3
		while visitor2 != 0:
			if self.g2.are_connected(visitor2,self.vis[i]):
				x1 = self.vis[i]%N
				y1 = self.vis[i]/N
				x2 = visitor2%N
				y2 = visitor2/N
				draw.line(self.window,(255,165,0),(x1*20+50,y1*20+50),(x2*20+50,y2*20+50),1)
				visitor = visitor2
				visitor2 = self.vis[i]

			i = i - 1		
	
	def search_path(self,start,end):
		self.vis.append(start)
		if not start == end:
			for i in range(self.g2.degree()[start]):
				if not self.g2.vs[start].neighbors()[i].index in self.vis:
					self.stack.append(self.g2.vs[start].neighbors()[i].index)
			c = self.stack[-1]
			self.stack.remove(c)
			self.search_path(c,end)
		

def main():
	init()

	maze = Maze()
	end = False
	while not end:
		for ev in event.get():
			if ev.type ==QUIT:
				end=True
		


		maze.clock.tick(20)
		display.flip()
	
if __name__ == "__main__":
    main()