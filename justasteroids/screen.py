import math

class Screen():
	""" Class that holds the frame buffer and implements drawing functions """
	
	def __init__(self,height,width) -> None:
		self.height, self.width = height, width
		self.scene = [['▒' for _ in range(width)]  for _ in range(height)]
		self.frameBuffer = self._newFrame()

	def _newFrame(self):
		return [line.copy() for line in self.scene]

	def newFrame(self):
		self.frameBuffer = self._newFrame()

	def drawString(self,x,y,stringList):
		print(f'\x1b[{x}B',end='')
		for line in stringList: print(f'\x1b[{y}C'+line)

	def draw(self,x,y,c):
		if 0 <= x < self.height and 0 <= y < self.width:
			self.frameBuffer[x][y] = c
	
	def drawLine(self,x1,y1,x2,y2,c):
		x1, y1, x2, y2 = round(x1), round(y1), round(x2), round(y2)
		if abs(x2-x1) >= abs(y2-y1): # If x-axis predominates
			if x2 <= x1: # In case x-axis goes left<-right, swap ends
				x1, x2 = x2, x1
				y1, y2 = y2, y1
			#Draw low
			dx, dy = (x2 - x1), (y2 - y1)

			yi = 1
			if dy < 0:
				yi = -1
				dy = -dy

			d = (2 * dy) - dx
			y = y1

			for x in range(x1,x2+1):
				self.draw(x,y,c)

				if d >= 0:
					y += yi
					d += (2 * (dy - dx))
				else:
					d += 2*dy
		else:
			if y2 <= y1: # In case y-axis goes down->up, swap ends
				x1, x2 = x2, x1
				y1, y2 = y2, y1
			#Draw high
			dx, dy = (x2 - x1), (y2 - y1)

			xi = 1
			if dx < 0:
				xi = -1
				dx = -dx

			d = (2 * dx) - dy
			x = x1

			for y in range(y1,y2+1):
				self.draw(x,y,c)

				if d > 0:
					x += xi
					d += (2 * (dx - dy))
				else:
					d += 2*dx

	def drawWireFrameModel(self,model,x,y,angle,scale,c):
		newModel = [point for point in model]

		for i, (mx, my) in enumerate(newModel): # Rotating coordinates
			rx = mx*math.cos(angle) - my*math.sin(angle)
			ry = mx*math.sin(angle) + my*math.cos(angle)
			newModel[i] = (rx,ry)

		for i, (mx, my) in enumerate(newModel): # Scaling model by scale factor
			newModel[i] = (mx*scale, my*scale)
		
		for i, (mx, my) in enumerate(newModel): # Placing coordinates
			newModel[i] = (mx+x,my+y)
		
		pointQty = len(newModel)
		for i, point in enumerate(newModel): # Drawing model line to line
			nxPoint = newModel[(i+1)%pointQty] # Modulo assures that we don't miss the (lastpoint,firstpoint) pair!
			self.drawLine(*point,*nxPoint,c)

	def display(self):
		""" Convert frame buffer to a string then print it to display a single frame """
		out = '\n'.join([''.join(line) for line in self.frameBuffer])+'\x1b[H'
		print(out)