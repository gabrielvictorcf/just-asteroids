import math

class SpaceObject():
	""" Class for every moving and interactible Space Object """
	
	def __init__(self,x,y,angle,dx,dy,wfmodel,size) -> None:
		self.x, self.dx = x, dx
		self.y, self.dy = y, dy
		self.angle = angle
		self.size = size
		self.wfmodel = wfmodel # WireFrame model consisting of a list of coordenate pairs
	
	def rotate(self,elapsedTime,angle):
		self.angle += angle*elapsedTime

	def accelerate(self,elapsedTime):
		self.dx += math.sin(self.angle) * 25.0 * elapsedTime
		self.dy -= math.cos(self.angle) * 25.0 * elapsedTime
	
	def move(self,elapsedTime):
		self.x += self.dx * elapsedTime
		self.y += self.dy * elapsedTime
	
	def brake(self):
		self.dx, self.dy = 0, 0