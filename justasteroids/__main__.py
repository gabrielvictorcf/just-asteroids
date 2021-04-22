import keyboard, time, os, math, random
from screen import Screen
from spaceobject import SpaceObject

title =  [r'                           ___   ___  ___   ________   _________                                    ']
title += [r'                           |\  \ |\  \|\  \ |\   ____\ |\___   ___\                                 ']
title += [r'                           \ \  \\ \  \\\  \\ \  \___|_\|___ \  \_|                                 ']
title += [r'                         __ \ \  \\ \  \\\  \\ \_____  \    \ \  \                                  ']
title += [r'                        |\  \\_\  \\ \  \\\  \\|____|\  \    \ \  \                                 ']
title += [r'                        \ \________\\ \_______\ ____\_\  \    \ \__\                                ']
title += [r'                         \|________| \|_______||\_________\    \|__|                                ']
title += [r'                                               \|_________|                                         ']
title += [r' ________   ________   _________   _______    ________   ________   ___   ________   ________       ']
title += [r'|\   __  \ |\   ____\ |\___   ___\|\  ___ \  |\   __  \ |\   __  \ |\  \ |\   ___ \ |\   ____\      ']
title += [r'\ \  \|\  \\ \  \___|_\|___ \  \_|\ \   __/| \ \  \|\  \\ \  \|\  \\ \  \\ \  \_|\ \\ \  \___|_     ']
title += [r' \ \   __  \\ \_____  \    \ \  \  \ \  \_|/__\ \   _  _\\ \  \\\  \\ \  \\ \  \ \\ \\ \_____  \    ']
title += [r'  \ \  \ \  \\|____|\  \    \ \  \  \ \  \_|\ \\ \  \\  \|\ \  \\\  \\ \  \\ \  \_\\ \\|____|\  \   ']
title += [r'   \ \__\ \__\ ____\_\  \    \ \__\  \ \_______\\ \__\\ _\ \ \_______\\ \__\\ \_______\ ____\_\  \  ']
title += [r'    \|__|\|__||\_________\    \|__|   \|_______| \|__|\|__| \|_______| \|__| \|_______||\_________\ ']
title += [r'              \|_________|                                                             \|_________| ']

def wrapCoords(x,y,sHei,sWid):
	if x < 0: x += sHei
	elif x >= sHei: x %= sHei

	if y < 0: y += sWid
	elif y >= sWid: y %= sWid

	return x, y

def genAsteroid(x,y,angle,dx,dy,pointQty,size):
	asteroidModel = []
	for i in range(pointQty):
		radius = (random.random() * 0.4) + 0.8
		angle = i/pointQty * 2 * math.pi
		px, py = radius*math.sin(angle), radius*math.cos(angle)
		asteroidModel.append((px,py))

	return SpaceObject(x,y,angle,dx,dy,asteroidModel,size)

def isPointInCircle(x,y,radius,xc,yc):
	# return math.sqrt((x-xc)**2 + (y-yc)**2) < radius
	return math.sqrt((x-xc)*(x-xc) + (y-yc)*(y-yc)) < radius

def getKeys(keys):
	return [keyboard.is_pressed(key) for key in keys] 

class AsteroidsGame(Screen):
	def __init__(self, height, width) -> None:
		super().__init__(height, width)
	
	def draw(self, x, y, c): # Overrtide draw function for toroidal wrapping
		x, y = wrapCoords(x,y,self.height,self.width)
		super().draw(x, y, c)
	
	def closeGame(self,ship,tile):
		self.drawWireFrameModel(ship.wfmodel,ship.x,ship.y,ship.angle,1,tile)
		self.display()
		time.sleep(5)
		print('\x1b[?25h\x1b[?47l\x1b[0J',end='') # Make cursor visible, restore and clear
		exit(0)

def main():
	# Initialize Game Variables
	screen = AsteroidsGame(100,300)
	greenTile, redTile, yellowTile = '\x1b[32m█\x1b[0m', '\x1b[31m█\x1b[0m', '\x1b[33m█\x1b[0m' # Ansi color codes

	triangleModel = [(-2.5,2.5),(0,-5),(2.5,2.5)] # Isoceles triangle wireframe model
	ship = SpaceObject(screen.height//2,screen.width//2,0,0,0,triangleModel,1)
	ship.isDead = False

	bullets = []

	asteroids = [genAsteroid(30,40,0,3,10,20,16), genAsteroid(60,240,0,-1,-15,20,16)]
	childAsteroids = [] # Asteroid buffer for when an asteroid is destroyed
	childQty = 3 # How many children an asteroid spawns when destroyed

	# Set up game screen - 1. Clear 2. Hide Cursor 3. Draw title
	os.system('cls' if os.name == 'nt' else 'clear')
	print('\x1b[?25l\x1b[=14h',end='')
	screen.drawString(42,100,title)

	# Await until player ready
	keyboard.wait('enter')
	print('\x1b[H',end='') # Restore cursor to (0,0)

	framesPerSecond = 60 # Game tick rate
	period = 1/framesPerSecond # Thread sleep time

	# Game loop
	t1 = time.time()
	while True:
		if ship.isDead: screen.closeGame(ship,redTile) # Kill player and close game
		
		t2 = time.time() # Game timing
		elapsedTime = t2-t1
		t1 = t2

		keys = getKeys(['left','up','right','space','b'])
		screen.newFrame()

		# Ship game logic
		pAngle = 5*keys[0] - 5*keys[2] # +5 if isLeftPressed | -5 if isRightPressed
		ship.rotate(elapsedTime,pAngle)
		if keys[1]: ship.accelerate(elapsedTime)
		ship.move(elapsedTime)
		if keys[4]: ship.brake() # Full halt

		if keys[3]: # Instantiate a bullet out of player
			bullet = SpaceObject(ship.x,ship.y,0,50*math.sin(ship.angle),-50*math.cos(ship.angle),None,1)
			bullets.append(bullet)

		ship.x, ship.y = wrapCoords(ship.x,ship.y,screen.height,screen.width)

		# Asteroid game logic
		for ast in asteroids:
			if isPointInCircle(ship.x,ship.y,ast.size,ast.x,ast.y):
				ship.isDead = True # Check player collision, if true then game over

			ast.move(elapsedTime)
			ast.rotate(elapsedTime,2.5)
			ast.x, ast.y = wrapCoords(ast.x,ast.y,screen.height,screen.width)

			screen.drawWireFrameModel(ast.wfmodel,ast.x,ast.y,ast.angle,ast.size,greenTile)
		
		# Bullet game logic
		for bullet in bullets:
			bullet.move(elapsedTime)
			for ast in asteroids:
				if not isPointInCircle(bullet.x,bullet.y,ast.size,ast.x,ast.y): continue

				bullet.x -= 500 # Throw bullet out of gamespace for removal

				if ast.size > 4: # Create child asteroids with half the size
					for _ in range(childQty):
						angle = random.random()*2*math.pi

						# Generate random offsets in range [-3,3]
						xoff, yoff = (random.random()*6)-3, (random.random()*6)-3

						dx, dy = 10*math.sin(angle)+xoff, 10*math.cos(angle)+yoff
						child = genAsteroid(ast.x+xoff,ast.y+yoff,0,dx,dy,20,ast.size>>1)
						childAsteroids.append(child)

				ast.x -= 1000 # Throw asteroid out of game space for removal
				break # Go to next bullet

		# Empty child asteroids buffer into actual asteroids list
		if childAsteroids:
			for _ in range(len(childAsteroids)): asteroids.append(childAsteroids.pop())

		# Destroy elements out of game space!
		asteroids = list(filter(lambda a: a.x > 0,asteroids))
		bullets = list(filter(lambda b: 0 <= b.x < screen.height and 0 <= b.y < screen.width,bullets))
		
		if not asteroids: screen.closeGame(ship,yellowTile) # Player victory!

		# Draw and display
		for bullet in bullets:
			bx, by = round(bullet.x), round(bullet.y)
			screen.draw(bx,by,greenTile)

		screen.drawWireFrameModel(ship.wfmodel,ship.x,ship.y,ship.angle,1,greenTile)

		screen.display()
		time.sleep(period)

if __name__ == '__main__':
	main()