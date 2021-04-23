# <p align="center"> <img src="https://i.imgur.com/xW65plv.png"> </p>

<img src="https://i.imgur.com/wjBAdaV.png" alt="img" align="right" width="400px">

Just asteroids is a clone of 'Atari Asteroids' rendered and played
entirely on the terminal with it's own game engine. It was made out
of curiosity on how a computer draws lines or objects to the screen,
and how those are interactible.

With that in mind, what better way to learn that besides
making a small game engine and game!

Also, check out [Javidx9's](https://www.youtube.com/channel/UC-yuWVUplUJZvieEligKBkA) channel! My implementation
is inspired on his video about [asteroids](https://www.youtube.com/watch?v=QgDR8LrRZhk).

## Installing
just-asteroids uses python's `keyboard` module, so although a regular
install will suffice on windows, linux will need a root install

### Pip install
	# use sudo if on linux
	pip install git+https://github.com/gabrielvictorcf/just-asteroids#egg=justasteroids

### Manual/Git install
	git clone https://github.com/gabrielvictorcf/just-asteroids
	cd just-asteroids
	pip3 install . # sudo pip3 install . if on Linux

## How to play
As of now, just-asteroids requires some manual adjustments:
- Resize terminal window: 305 columns x 105 rows
- Change font size to 6

After that, just open the game and press `enter` when you're ready!

## Controls
```
enter: start game
left-arrow: left rotate
right-arrow: right rotate
up: thrust
space: shoot
b: brake
```