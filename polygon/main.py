import matplotlib.pyplot as plt
from numpy import sin,cos,radians

	
def polygon(s):
	result = ""
	for i in range(len(s)-1,-1,-1):
		result = result + s[i]
	return result

class polygon(object):
	def __init__(self,v = [0,0]):
		self.vertex = v
	
	def points(self):
		for v in self.vertex:
			print(v)
			
	def translate(self,x,y):
		for i in range(len(self.vertex)):
			self.vertex[i] = [self.vertex[i][0]+x,self.vertex[i][1]+y]
			
	def rotate(self,x,y,a):
		self.translate(-x,-y)
		for i in range(len(self.vertex)):
			self.vertex[i] = [self.vertex[i][0]*cos(a)-self.vertex[i][1]*sin(a),self.vertex[i][0]*sin(a)+self.vertex[i][1]*cos(a)]
		self.translate(x,y)
	
	def draw(self):
		for i in range(len(self.vertex)):
			plt.plot([self.vertex[i][0], self.vertex[i-1][0]], [self.vertex[i][1], self.vertex[i-1][1]], 'b-',lw=2)

def main():
	
	pol = polygon([[10,10],[20,20],[15,20]])
	pol.points()
	pol.draw()
	
	
	print("Translate (30,20):")
	pol.translate(30,20)
	pol.points()
	pol.draw()
	
	print("Rotate 30 degrees around (50,50): ")
	pol.rotate(50,50,radians(30))
	pol.points()
	pol.draw()
	
	for i in range(12):
		pol.rotate(50,50,radians(30))
		pol.points()
		pol.draw()
	
	plt.show()
if __name__ == "__main__":
    main()